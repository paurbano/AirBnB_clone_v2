#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
ALIAS="\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
SRC="/etc/nginx/sites-enable/default"
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
echo "<html><head><\head><body>Hello World from:..<\body><\html>" > /data/web_static/releases/test/index.html
if [ -L "/data/web_static/current" ]
then
    sudo rm "/data/web_static/current"
else
    sudo ln -s /data/web_static/releases/test/ /data/web_static/current
fi
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "30i $ALIAS" $SRC
sudo service nginx restart
