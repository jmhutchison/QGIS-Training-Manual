# -*- mode: ruby -*-
# vi: set ft=ruby :

#


Vagrant.configure("1") do |config|
  config.vm.network :bridged
end

Vagrant.configure("2") do |config|
  config.vm.box = "Ubuntu precise 64"
  config.vm.hostname = "qgis"
  config.vm.network :public_network
  config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

end
