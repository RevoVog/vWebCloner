#!/usr/bin/env bash
set -euo pipefail

# Must run as root
if [ "$(id -u)" -ne 0 ]; then
  echo "Please run as root (sudo)."
  exit 1
fi

# 1) Install apache2
apt update
apt install -y apache2

# 2) Enable CGI module & restart
a2enmod cgi || true

# 3) Copy index.html to webroot (backup existing)
if [ -f /var/www/html/index.html ]; then
  cp /var/www/html/index.html /var/www/html/index.html.bak.$(date +%s) || true
fi
cp ./index.html /var/www/html/index.html
chown www-data:www-data /var/www/html/index.html

# 4) Put CGI script in /usr/lib/cgi-bin (Apache default cgi dir)
mkdir -p /usr/lib/cgi-bin
cp ./cgi-bin/login.py /usr/lib/cgi-bin/login.py
chmod 755 /usr/lib/cgi-bin/login.py
chown root:root /usr/lib/cgi-bin/login.py

# 5) Restart apache
systemctl restart apache2

echo "Apache installed and started. index.html served at http://localhost/"
echo "CGI available at http://localhost/cgi-bin/login.py"
