FROM ubuntu:14.04

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y zip unzip tzdata curl
RUN apt-get install -y php5
RUN apt-get install -y apache2 libapache2-mod-php5

RUN rm /var/www/html/index.html
COPY ./src /var/www/html/
RUN chmod 777 /var/www/html/upload/
COPY ./run-lamp.sh /usr/sbin/
COPY ./000-default.conf /etc/apache2/sites-enabled/

RUN a2enmod rewrite
RUN chmod +x /usr/sbin/run-lamp.sh

# FLAG
COPY ./flag.c /flag.c
RUN apt install -y gcc \
    && gcc /flag.c -o /flag \
    && chmod 111 /flag && rm /flag.c

EXPOSE 80

CMD ["/usr/sbin/run-lamp.sh"]