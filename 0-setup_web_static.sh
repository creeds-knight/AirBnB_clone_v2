#!/usr/bin/env bash
# A bash script to setup webservers for the deployment of web_static
#Installing nginx
if ! dpkg -l | grep nginx; then
	sudo apt-get update
	sudo apt-get -y install nginx
fi
#creating folders

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#creating test file

echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
#updating nginx configuration

echo "server{
    listen 80 default_server;
    root /var/www/html;
    add_header X-Served-By $HOSTNAME;

    location /redirect_me {
    	return 301 https://www.google.com;
    }
    error_page 404 /custom_404.html;

    location /hbnb_static {
    	alias /data/web_static/current/;
	index index.htm index.html;
    }
}" > /etc/nginx/sites-available/default


#restarting nginx

sudo service nginx restart
exit 0
