#! /usr/bin/env bash

export MYSQL_USER=dbuser 
export MYSQL_PASSWORD=dbpass

/usr/bin/mysqld_safe --timezone=${DATE_TIMEZONE}&
python app.py