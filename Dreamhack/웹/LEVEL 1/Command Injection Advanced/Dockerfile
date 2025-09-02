FROM ubuntu:20.04

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y zip unzip tzdata curl
RUN apt-get install -y  \
  php \
  php-fpm

RUN apt-get install apache2 libapache2-mod-php -y

RUN rm /var/www/html/index.html
COPY ./deploy/src /var/www/html/
RUN chmod 777 /var/www/html/cache/
COPY ./deploy/run-lamp.sh /usr/sbin/

RUN a2enmod rewrite
RUN chmod +x /usr/sbin/run-lamp.sh

# FLAG
COPY deploy/flag.c /flag.c
RUN apt install -y gcc \
    && gcc /flag.c -o /flag \
    && chmod 111 /flag && rm /flag.c


EXPOSE 80

CMD ["/usr/sbin/run-lamp.sh"]