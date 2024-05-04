#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment

# Install Nginx if it not already installed
sudo apt update -y 
sudo apt install nginx -y

# Create the folders and file /data/web_static/releases/test/index.html if doesn’t exist(with simple content, to test your Nginx configuration)
mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html
# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder; If symbolic link already exists, it should be deleted and recreated every time the script is ran.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group; This should be recursive;
sudo chmod -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Don’t forget to 
echo "server{
        location hbnb_static{
            alias /data/web_static/current/;
        }
    }" | sudo tee /etc/nginx/sites-available/default > /dev/null

# restart Nginx after updating the configuration
sudo service nginx restart
