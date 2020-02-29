#!/bin/bash
yum update -y
yum install -y vim setroubleshoot-server tcpdump git

# Setup Docker
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install -y docker-ce docker-ce-cli containerd.io
curl -L "https://github.com/docker/compose/releases/download/1.25.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
curl -L https://raw.githubusercontent.com/docker/compose/1.25.4/contrib/completion/bash/docker-compose -o /etc/bash_completion.d/docker-compose

# Setup Environment
mkdir /data
mkdir /srv

# Get Django Code
ssh-keygen -q -t rsa -P '' -f ~/.ssh/id_rsa
echo -e 'Add the following key to github app keys for repo:\n\n'
cat /root/.ssh/id_rsa.pub
echo -e '\n'
read -p "Press enter to continue"

git clone git@github.com:valinkrai/django-personal-website.git /srv/

# Setup user and permissions
useradd -d /srv jenkins
usermod -aG docker jenkins
chmod 0700 /srv/
mkdir /srv/.ssh
chmod 700 /srv/.ssh/
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDH3WexN6yX7mEXbMzca9j3C+0AH23CbotAKZMxji9QRKNERChYHlilpkwWiyS4QtCMq+u8p61TqJowmbErDNIQ3AFfWqWdg6+SlFKrJwnH2IDaWpMZFg2FM7o57Oz4cvYi/qBjHnIqQiDQAHR+rClAA5Ui76tm6wVwgKj0iyEyMwMY9Eikklzb+RRYpoEpPet0hANB+JHa74w88S7cj1ZMs0yJ8W1M0sgx1scboJ1/w+DAHizttX49hoEcvEGEfA+aLOhOz6eOi0FTpRBbJhdO8OhG6TLOyj8vGsJgbWVlEY+KpFyqQ1emA5TVeNg9MJ09LcRTqmEcIL9n7N1m/vyf jenkins@alan.thegrid.trenton.io' > /srv/.ssh/authorized_keys
mv ~/.ssh/* /srv/.ssh/
chmod 0700 /srv/.ssh/
chmod 600 /srv/.ssh/*
chown -R jenkins:jenkins /srv /data

# Set selinux context
chcon -R unconfined_u:object_r:user_home_t:s0 /srv/

# Tell user to 