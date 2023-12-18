# INSTALLATION GITHUB
# update repo
sudo apt-get update

# upgrade package
sudo apt-get upgrade

# install git
sudo apt-get install git

# git clone 
git clone https://github.com/hrdip/Django-Advanced-Blog.git

# delete ogild docker
sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-compose-plugin

# INSTALLATION DOCKER
# delete files
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd

# get script for install docker
curl -fsSL https://get.docker.com -o get-docker.sh

# install docker
sudo sh get-docker.sh

# make group
sudo groupadd docker

# add user to group
sudo usermod -aG docker $USER

# add new group
newgrp docker

# settings
sudo systemctl enable docker.service

# run docker
sudo systemctl enable containerd.service
# ??sudo systemctl enable docker images
# INSTALLATION DOCKER-COMPOSE
# install docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# change mood
sudo chmod +x /usr/local/bin/docker-compose

# check docker-compose
docker-compose --version

# Generating a new SSH key and adding it to the ssh-agent 
# going to destination directory and change email
ssh-keygen -t ed25519 -C "hrdip.2018@gmail.com"
# put empty password

# connected to ssh agent
eval "$(ssh-agent -s)"

# add key to settings
ssh-add ~/.ssh/id_ed25519

# get public key
cat .ssh/id_ed25519.pub

# copy that key and paste on SSH and GPG keys into main settings of github

# CLONE OUR REPOSITORIES TO PUTTY
git clone <our repo ssh code>

# change directory to our repo
cd Django-Advanced-Blog/

# run docker-compose
docker-compose -f docker-compose-stage.yml up --build -d

# Installing Nginx
sudo apt update
sudo apt install nginx

# Adjusting the Firewall
sudo ufw app list

# You can enable this by typing
sudo ufw allow 'Nginx HTTP'

# You can verify the change by typing
sudo ufw status

# if status disable
sudo ufw enable

# Checking your Web Server
systemctl status nginx

# if is not active
sudo fuser -k 80/tcp
sudo fuser -k 443/tcp
sudo service nginx restart

# get url for connection
curl -4 icanhazip.com