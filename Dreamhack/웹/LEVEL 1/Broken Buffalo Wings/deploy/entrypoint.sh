#!/bin/sh
chmod 600 /entrypoint.sh

/usr/bin/supervisord -c /etc/supervisord.conf