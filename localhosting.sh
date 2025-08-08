#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: ./host_html.sh <file.html>"
    exit 1
fi

FILE=$1
APACHE_DIR="/var/www/html"

# Check if Apache2 installed
if ! command -v apache2 >/dev/null 2>&1; then
    echo "[✘] Apache2 is not installed. Installing..."
    sudo apt update && sudo apt install apache2 -y
fi

# Copy file to Apache web directory
if [ -f "$FILE" ]; then
    sudo cp "$FILE" "$APACHE_DIR"
    echo "[✔] File copied to Apache directory."
else
    echo "[✘] File not found!"
    exit 1
fi

# Start Apache2 service
sudo systemctl enable apache2
sudo systemctl start apache2

echo "[✔] Hosting file at: http://localhost/$FILE"
