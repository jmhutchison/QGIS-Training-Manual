|LS| Installing and Managing Plugins
===============================================================================

To begin using plugins, you need to know how to download, install and activate
them. To do this, you will learn how to use the :guilabel:`Plugin Installer`
and :guilabel:`Plugin Manager`.

**The goal for this lesson:** To understand and use QGIS' plugin system.

|basic| |FA| Managing Plugins
-------------------------------------------------------------------------------

* To open the :guilabel:`Plugin Manager`, click on the menu item
  :menuselection:`Plugins --> Manage Plugins`.
* The following dialog will open, showing the different plugins already installed 
in your QGIS software. What you see may differ slightly to the image below, depending 
upon what plugins you have installed:

  .. image:: ../_static/qgis_plugins/005.png
     :align: center

You can activate or deactivate these plugins by clicking on their corresponding 
check box.

The list of plugins that you can activate and deactivate only draws from the plugins 
that you currently have installed. To install new plugins, you need to use the 
:guilabel:`Plugin Installer`.

|basic| |FA| Installing New Plugins
-------------------------------------------------------------------------------

* To start the :guilabel:`Plugin Installer`, click on the menu item
  :menuselection:`Plugins --> Fetch Python Plugins`.

A dialog will appear. The amount of plugins that you see here will differ,
depending on your setup.

QGIS plugins are stored online in repositories. By default, only the official
repositories are active, meaning that you can only access official plugins.
These are usually the first plugins you want, because they have been tested
thoroughly and are often included in QGIS by default.

It is possible, however, to try out more plugins than the default ones. To do this:

* Open the :guilabel:`Options` tab on the :guilabel:`Plugin Installer`
  dialog:
  
  .. image:: ../_static/qgis_plugins/002.png
     :align: center

* Click the :guilabel:`Show all plugins except those marked as experimental` option.

If you want to, you can click on the :guilabel:`Show all plugins, even those marked as 
experimental` option. Be aware that experimental plugins may not be fully tested.

* Now go back to the :guilabel:`Plugins` tab to find the available plugins.

  .. image:: ../_static/qgis_plugins/003.png
     :align: center

* To install a plugin, simply click on it in the list and then click the
  :guilabel:`Install plugin` button.

|IC|
-------------------------------------------------------------------------------

Installing plugins in QGIS is simple.

|WN|
-------------------------------------------------------------------------------

Next we will introduce you to some useful plugins as examples.
