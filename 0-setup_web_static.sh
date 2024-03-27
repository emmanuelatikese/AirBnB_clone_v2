#!/usr/bin/env bash
#creating files and making nginx configs
if ! command -v nginx &> /dev/null; then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

if [ ! -d "/data/" ]; then
	sudo mkdir -p /data/web_static/{releases/test,shared}
	sudo touch /data/web_static/releases/test/index.html

fi
echo "html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

if [ -L "/data/web_static/current" ]; then
	sudo rm /data/web_static/releases/test/
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo tee /etc/nginx/sites-available/default <<EOF
server {
    listen 80 default_server;
    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
    }

    location / {
        add_header X-Served-By \$hostname;
        return 200 "Hello, this is Nginx serving your web content!";
    }
}
EOF

sudo service nginx restart
