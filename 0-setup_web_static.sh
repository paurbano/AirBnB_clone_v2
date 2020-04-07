#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
ALIAS="\\\tlocation /hbnb_static/ {\n\t\t alias /data/web_static/current/;\n\t}\n"
SRC="/etc/nginx/sites-available/default"
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
echo "<html><head><\head><body> Holberton School<\body><\html>" > /data/web_static/releases/test/index.html
if [ -L "/data/web_static/current" ]
then
    ubuntu rm "/data/web_static/current"
else
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current
    sudo chown 
fi
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "30i $ALIAS" $SRC
sudo service nginx restart
