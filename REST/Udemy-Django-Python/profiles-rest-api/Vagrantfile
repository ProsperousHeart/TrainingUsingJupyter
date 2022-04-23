# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
 # The most common configuration options are documented and commented below.
 # For a complete reference, please see the online documentation at
 # https://docs.vagrantup.com.

 # Every Vagrant development environment requires a box. You can search for
 # boxes at https://vagrantcloud.com/search.
 # config.vm.box = "ubuntu/xenial64"
 config.vm.box = "ubuntu/bionic64"
 config.vm.box_version = "~> 20200304.0.0"

 config.vm.network "forwarded_port", host_ip: "127.0.0.1", guest: 8000, host: 8000
 config.vm.provision "shell", inline: <<-SHELL
   systemctl disable apt-daily.service
   systemctl disable apt-daily.timer

   # Update and upgrade the server packages.
   sudo apt-get update
   sudo apt-get -y upgrade
   # Set Ubuntu Language
   sudo locale-gen en_GB.UTF-8

   # Upgrade pip to the latest version.
   sudo apt-get install -y python-pip
   sudo pip install --upgrade pip

   sudo apt-get install -y python3-venv zip
   touch /home/vagrant/.bash_aliases
   if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
     echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
     echo "alias python='python3'" >> /home/vagrant/.bash_aliases
   fi
   # Install Python, SQLite and pip
   # sudo apt-get install -y python3-dev sqlite python-pip
  #  sudo apt-get install -y sqlite python-pip
  sudo apt-get install -y sqlite
   # Install and configure python virtualenvwrapper.
   sudo pip install virtualenvwrapper
   if ! grep -q VIRTUALENV_ALREADY_ADDED /home/vagrant/.bashrc; then
       echo "# VIRTUALENV_ALREADY_ADDED" >> /home/vagrant/.bashrc
       echo "WORKON_HOME=~/.virtualenvs" >> /home/vagrant/.bashrc
       echo "PROJECT_HOME=/vagrant" >> /home/vagrant/.bashrc
       echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/vagrant/.bashrc
   fi
 SHELL

end
