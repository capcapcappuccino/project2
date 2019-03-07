Overview
--------

This is a project develops a Sports Catalog that provides a list of  sports and sport items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

Getting Started
---------------

The dependencies are:
1) Set up Virtual Linux Machine on PC - VirtualBox, which you can get from: https://www.virtualbox.org/wiki/Downloads
									 	Vagrant, which you can get from: https://www.vagrantup.com/downloads.html
2) On Windows, install Git Bash as your terminal.

Installation
------------
1) Once you have VirtualBox and Vagrant installed, open a terminal and run the following commands:
   	mkdir news
   	cd news
   	vagrant init ubuntu/trusty64
   	vagrant up
   	vagrant ssh
2) run python database_setup.py
3) run lotsofspecificSport.py
4) Database sportspecificSport.db will be created

Running the Script
-------------------

To run the script: 'python project.py'

The script will then be running and you can view the application in localhost:8000

Go to browser and type localhost:8000, and you'll be able to play with the application.

Go to login with your google or facebook account, and you can create / edit / delete items.
