FROM python:3.10-slim-bullseye

ENV USER buffer_wing
ENV PORT 8000
RUN adduser --disabled-password $USER

RUN apt-get update && apt-get install -y supervisor nginx gnupg2 python3-pip build-essential wget curl unzip lsb-release

RUN curl -fsSL https://packages.sury.org/php/apt.gpg | tee /etc/apt/trusted.gpg.d/php.gpg > /dev/null
RUN echo "deb https://packages.sury.org/php/ $(. /etc/os-release && echo $VERSION_CODENAME) main" | tee /etc/apt/sources.list.d/php.list

RUN apt-get update && apt-get install -y php7.4-fpm && \
    rm -rf /var/lib/apt/lists/*


## chrome
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gnupg \
        ca-certificates \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y \
        google-chrome-stable \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

## chromedriver
RUN wget https://storage.googleapis.com/chrome-for-testing-public/`curl -sS https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE`/linux64/chromedriver-linux64.zip \
    && unzip chromedriver-linux64.zip \
    && rm chromedriver-linux64.zip



RUN sed -i '215s/4096/8192/' /etc/php/7.4/fpm/php.ini
RUN service php7.4-fpm restart

COPY  ./config/fpm.conf /etc/php/7.4/fpm/php-fpm.conf
COPY  ./config/supervisord.conf /etc/supervisord.conf
COPY  ./config/nginx.conf /etc/nginx/nginx.conf


WORKDIR /app


COPY --chown=$USER:$USER . /app

RUN pip3 install -r ./bot/requirements.txt
RUN chmod +x bot/bot.py

EXPOSE $PORT

COPY --chown=root entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]