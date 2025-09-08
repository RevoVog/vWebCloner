#!/usr/bin/env bash
set -euo pipefail

if [ "$(id -u)" -ne 0 ]; then
  echo "Run as root (sudo)."
  exit 1
fi

apt update
apt install -y apache2

a2enmod cgi || true

# Put HTML
cp ./index.html /var/www/html/index.html
chown www-data:www-data /var/www/html/index.html

# Put CGI
mkdir -p /usr/lib/cgi-bin
cp ./cgi-bin/login.py /usr/lib/cgi-bin/login.py
chmod 755 /usr/lib/cgi-bin/login.py

# FIFO for passing submissions
if [ ! -p /tmp/login_fifo ]; then
  mkfifo /tmp/login_fifo
  chmod 666 /tmp/login_fifo
fi

systemctl restart apache2
