#!/bin/bash

#. /etc/lsb_release
#OS=$DISTRIB_ID
#VER=$DISTRIB_RELEASE

#if [[ "$OS" != "Ubuntu"]] || [[ "$VER" != "14.04" ]]; then
#	echo "Unsupported OS installed!"
#	exit
#fi

echo "Running modemscripts setup..."

apt-get update
apt-get install git
apt-get install ppp
apt-get install python-dev python-pip
pip install wiringpi2
pip install pyserial

#apt-get install openssh-server
#apt-get install expect

git clone https://github.com/johncobb/modemscripts.git /home/pi/apps/modemscripts2

# Copy PPP dependencies
cp /apps/modemscripts/etc/ppp/options /etc/ppp/options
cp /apps/modemscripts/etc/ppp/peers/*.* /etc/ppp/peers
cp /apps/modemscripts/etc/ppp/ip-up.d/addroute /etc/ppp/ip-up.d/addroute

# copy service descriptor to systemd folder
cp /apps/modemscripts/systemd/enablemodem.service /etc/systemd/system/enablemodem.service

systemctl enable enablemodem.service
systemctl start enablemodem.service
systemctl daemon-reload

#reboot
