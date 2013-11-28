#!/bin/python
# ~/fabfile.py
# A Fabric file for carrying out various administrative tasks.
# Tim Sutton, Jan 2013

# To use this script make sure you have fabric and fabtools.
# pip install fabric fabtools

import os
from fabric.api import run, sudo, env, hide, cd, task, fastprint
from fabric.colors import red, magenta, yellow, cyan
from fabric.contrib.files import contains, exists, append, sed
from fabric.context_managers import quiet
import fabtools
from fabgis import postgres, common, virtualenv, git
#umn_mapserver
# Don't remove even though its unused
#noinspection PyUnresolvedReferences
from fabtools.vagrant import vagrant

# Usage fab localhost [command]
#    or fab remote [command]
#  e.g. fab localhost update

# This will get replaced in various places, for a generic site, it may be
# all you need to change...
PROJECT_NAME = 'qgismanual'
#env.user = 'vagrant'


def _all():
    """Things to do regardless of whether command is local or remote."""

    # Key is hostname as it resolves by running hostname directly on the server
    # value is desired web site url to publish the repo as.

    repo_site_names = {'qgis-vagrant': 'localhost:8080'}

    with hide('output'):
        env.user = run('whoami')
        env.hostname = run('hostname')
        if env.hostname not in repo_site_names:
            print 'Error: %s not in: \n%s' % (env.hostname, repo_site_names)
            exit()
        else:
            # sitename for apache venv
            env.repo_site_name = repo_site_names[env.hostname]
            # where to check the repo out to
            env.webdir = '/home/web/'
            # repo uri
            env.git_url = 'https://github.com/qgis/QGIS-Training-Manual.git'
            # checkout name for repo
            env.repo_alias = PROJECT_NAME
            # user wsgi should run as (will be created if needed)
            env.wsgi_user = 'qgis'
            # Deploy dir - e.g. /home/web/foo
            env.code_path = os.path.join(env.webdir, env.repo_alias)
            show_environment()

###############################################################################
# Next section contains helper methods tasks
###############################################################################


@task
def rsync_vagrant_to_code_dir():
    """Rsync from vagrant mount to code dir."""
    _all()
    with cd('/home/web/'):
        sudo('rsync -va /vagrant/ %s/ --exclude \'venv\' '
             '--exclude \'*.pyc\' --exclude \'.git\'' % PROJECT_NAME)


def replace_tokens(conf_file):
    if '.templ' == conf_file[-6:]:
        conf_file = conf_file.replace('.templ', '')

    run(
        'cp %(conf_file)s.templ %(conf_file)s' % {
            'conf_file': conf_file})
    # We need to replace these 3 things in the conf file:
    # [SERVERNAME] - web site base url e.g. foo.com
    # [ESCAPEDSERVERNAME] - the site base url with escaping e.g. foo\.com
    # [SITEBASE] - dir under which the site is deployed e.g. /home/web
    # [SITENAME] - should match env.repo_alias
    # [SITEUSER] - user apache wsgi process should run as
    # [CODEBASE] - concatenation of site base and site name e.g. /home/web/app
    escaped_name = env.repo_site_name.replace('.', '\\\.')
    fastprint('Escaped server name: %s' % escaped_name)
    sed('%s' % conf_file, '\[SERVERNAME\]', env.repo_site_name)
    sed('%s' % conf_file, '\[ESCAPEDSERVERNAME\]', escaped_name)
    sed('%s' % conf_file, '\[SITEBASE\]', env.webdir)
    sed('%s' % conf_file, '\[SITENAME\]', env.repo_alias)
    sed('%s' % conf_file, '\[SITEUSER\]', env.wsgi_user)
    sed('%s' % conf_file, '\[CODEBASE\]', env.code_path)


@task
def setup_website():
    """Initialise or update the git clone.

    e.g. to update the server

    fab -H 10.1.1.0:8697 remote setup_website

    or if you have configured env.hosts, simply

    fab remote setup_website
    """
    _all()
    fabtools.require.deb.package('libapache2-mod-wsgi')
    # Find out if the wsgi user exists and create it if needed e.g.
    fabtools.require.user(
        env.wsgi_user,
        create_group=env.wsgi_user,
        system=True,
        comment='System user for running the wsgi process under')

    if not exists(env.webdir):
        sudo('mkdir -p %s' % env.plugin_repo_path)
        sudo('chown %s.%s %s' % (env.user, env.user, env.webdir))

    # Clone and replace tokens in apache conf

    conf_file = (
        '%s/resources/server_config/apache/%s.apache.conf' % (
            env.code_path, env.repo_alias))

    run(
        'cp %(conf_file)s.templ %(conf_file)s' % {
            'conf_file': conf_file})

    replace_tokens(conf_file)

    with cd('/etc/apache2/sites-available/'):
        if exists('%s.apache.conf' % env.repo_alias):
            sudo('a2dissite %s.apache.conf' % env.repo_alias)
            fastprint('Removing old apache2 conf', False)
            sudo('rm %s.apache.conf' % env.repo_alias)

        sudo('ln -s %s .' % conf_file)

    # Add a hosts entry for local testing - only really useful for localhost
    hosts = '/etc/hosts'
    if not contains(hosts, env.repo_site_name):
        append(hosts, '127.0.0.1 %s' % env.repo_site_name, use_sudo=True)
    if not contains(hosts, 'www.' + env.repo_site_name):
        append(hosts,
               '127.0.0.1 %s' % 'www.' + env.repo_site_name,
               use_sudo=True)
        # Make sure mod rewrite is enabled
    sudo('a2enmod rewrite')
    # Enable the vhost configuration
    sudo('a2ensite %s.apache.conf' % env.repo_alias)

    # Check if apache configs are ok - script will abort if not ok
    sudo('/usr/sbin/apache2ctl configtest')
    sudo('a2dissite default')
    fabtools.require.service.restarted('apache2')


def setup_venv():
    """Initialise or update the virtual environmnet.


    To run e.g.::

        fab -H 188.40.123.80:8697 remote setup_venv

    or if you have configured env.hosts, simply

        fab remote setup_venv
    """

    virtualenv.setup_venv(env.code_path, requirements_file='requirements.txt')

    # Run again to check all is up to date
    with cd(env.code_path):
        run('venv/bin/pip install -r requirements.txt')


@task
def update_git_checkout(branch='master'):
    """Make sure there is a read only git checkout.

    Args:
        branch: str - a string representing the name of the branch to build
            from. Defaults to 'master'

    To run e.g.::

        fab -H 188.40.123.80:8697 update_git_checkout


    """
    _all()
    git.update_git_checkout(
        env.web_dir, env.git_url, env.repo_alias, branch=branch)


@task
def build_docs(lang='en'):
    """
    Default build localisation is English. To build all localisations,
    run:

        fab <site_name> build_sphinx(lang=None)

    To build docs in specific localisation, run:

        fab <site_name> build_sphinx(lang='de ja ro')

    If no lang kwarg is provided, the docs will build in English only using
    'make html'. This is the default action.
    """
    _all()
    with cd(env.code_path):
        if lang:
            run('./post_translate.sh %s' % lang)
        else:
            run('./post_translate.sh')


@task
def deploy(branch='master'):
    """Do a fresh deployment of the site to a server.

    Args:
        branch: str - a string representing the name of the branch to build
            from. Defaults to 'master'.

    To run e.g.::

        fab -H 188.40.123.80:8697 deploy

        or to package up a specific branch (in this case v1)

        fab -H 88.198.36.154:8697 deploy:v1

    For live server:

        fab -H 5.9.140.151:8697 deploy

    """
    _all()
    fastprint(cyan('%s deploy task started...\n' % PROJECT_NAME))
    #with quiet():
    fabtools.require.deb.package('python-pip')
    fabtools.require.deb.package('python-dev')
    fabtools.require.deb.package('build-essential')
    fabtools.require.deb.package('python-sphinx')
    fabtools.require.deb.package('texlive-full')
    fabtools.require.deb.package('curl')
    fastprint(cyan('Updating GIT checkout...\n'))
    #with quiet():
    if not exists(env.webdir):
        sudo('mkdir -p %s' % env.plugin_repo_path)
        sudo('chown %s.%s %s' % (env.user, env.user, env.webdir))
    update_git_checkout(branch)
    fastprint(cyan('Setting up venv...\n'))
    #with quiet():
    setup_venv()
    fastprint(cyan('Setting up website...\n'))
    #with quiet():
    setup_website()
    if not fabtools.service.is_running('apache2'):
        fastprint(red(
            'Apache is not running - you may need to log in to '
            'start it manually.\n'))
    build_docs()
    fastprint(red('Build complete. Visit http://localhost/en/ to view the'
                  'English docs. If you wish to build the docs in an '
                  'alternative localistion, run e.g.'
                  '"fab vagrant build_docs(lang="de") and visit'
                  'http://localhost/de/'))


@task
def show_environment():
    """For diagnostics - show any pertinent info about server."""
    fastprint('\n-------------------------------------------------\n')
    fastprint(cyan('User      : %s\n' % env.user))
    fastprint(cyan('Host      : %s\n' % env.hostname))
    fastprint(cyan('Site Name : %s\n' % env.repo_site_name))
    fastprint(cyan('Dest Path : %s\n' % env.webdir))
    fastprint(cyan('Wsgi User : %s\n' % env.wsgi_user))
    fastprint(cyan('Git  Url  : %s\n' % env.git_url))
    fastprint(cyan('Repo Alias: %s\n' % env.repo_alias))
    fastprint(cyan('-------------------------------------------------\n'))
