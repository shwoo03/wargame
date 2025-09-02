FROM python:3.10-slim-buster

# ENV
ENV user dreamhack
ENV port 8000

RUN apt-get update && apt-get install -y python3-pip wget curl unzip gnupg2

## chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update -y && apt-get install -y google-chrome-stable
RUN wget https://chromedriver.storage.googleapis.com/`curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip && unzip chromedriver_linux64.zip && rm chromedriver_linux64.zip


# SET challenges
RUN adduser $user
ADD ./deploy /app
WORKDIR /app
RUN pip3 install -r requirements.txt

RUN chown root:$user /app/flag.txt

# RUN
USER $user
EXPOSE $port

ENTRYPOINT ["python3"]
CMD ["app.py"]

