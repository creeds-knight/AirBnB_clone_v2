#!/usr/bin/env bash
# A bash script to setup webservers for the deployment of web_static
#Installing nginx
sudo apt-get update
sudo apt-get -y install nginx
#creating folders

folders=("/data/" "/data/web_static/" "/data/web_static/releases/"
"/data/web_static/shared" "/data/web_static/releases/test/")
for i in "${folders[@]}"; do
	sudo mkdir -p "$i"
done

#creating test file

sudo echo "This is a test file" > /data/web_static/releases/test/index.html

ln-sf /data/web_static/current /data/web/static/releases/test/

sudo chown ubuntu:ubuntu /data/web_static/releases/test/index.html
#updating nginx configuration

echo "server{
    listen 80 default_server;
    root /var/www/html;
    add_header X-Served-By $HOSTNAME;


    location /hbnb_static {
    	alias /data/web_static/current/;
	index index.htm index.html;
    }
}" > /etc/nginx/sites-available/default

sudo ln -sf /etc/nginx/sites-available/web_static /etc/nginx/sites-enabled/

#restarting nginx

sudo service nginx restart
