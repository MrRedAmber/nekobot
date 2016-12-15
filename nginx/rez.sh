#!/bin/sh
echo [nginx] sleeping for 5 seconds
sleep 5
echo [nginx] restarting service
service nginx restart
echo [nginx] nginx is ready!
tail -f /tmp/access.log