FROM ubuntu:24.04

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y zip unzip tzdata curl
RUN apt-get install -y php
RUN apt-get install -y apache2

RUN rm /var/www/html/index.html
COPY ./deploy/src /var/www/html/ 
RUN chmod 777 /var/www/html/user/
RUN chmod 666 /var/www/html/user/*.json
COPY ./deploy/000-default.conf /etc/apache2/sites-enabled/
COPY ./deploy/.htaccess /var/www/html/user/
COPY ./deploy/run.sh /usr/sbin/
COPY ./deploy/flag /flag

RUN a2enmod rewrite
RUN a2enmod dav
RUN a2enmod dav_fs
RUN chmod +x /usr/sbin/run.sh

EXPOSE 80

CMD ["/usr/sbin/run.sh"]