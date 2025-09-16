FROM python:3.10-slim-buster

# ENV
ENV user dreamhack
ENV port 5000

# SET packages
RUN apt-get update -y && apt-get install -y python3-pip python-dev build-essential default-libmysqlclient-dev pkg-config
RUN apt-get install mariadb-common mariadb-server mariadb-client -y

# SET challenges
RUN adduser $user
ADD ./deploy /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN chmod +x run.sh

# DB
RUN /bin/bash -c "/usr/bin/mysqld_safe &" && \
  sleep 5 && \
  mysql -uroot < /app/init.sql
RUN rm /app/init.sql

# RUN
#USER $user
EXPOSE $port

CMD ["./run.sh"]