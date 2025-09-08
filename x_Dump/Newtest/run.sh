#!/bin/bash
# run.sh - quick Apache2 host for login form

# Ensure apache2 + CGI enabled
sudo apt-get update -y
sudo apt-get install -y apache2

sudo a2enmod cgi
sudo systemctl restart apache2

# Deploy files
sudo cp index.html /var/www/html/
sudo mkdir -p /usr/lib/cgi-bin
sudo cp submit.sh /usr/lib/cgi-bin/
sudo chmod +x /usr/lib/cgi-bin/submit.sh

# Prepare log file
sudo touch /tmp/login_capture.log
sudo chmod 666 /tmp/login_capture.log

echo "========================================"
echo " Server running at: http://localhost/ "
echo " Submissions will appear below... "
echo "========================================"

# Tail logs so responses show up in terminal
tail -f /tmp/login_capture.log
