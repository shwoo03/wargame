FROM python:3-alpine

ENV user chall
ENV port 3000

RUN apk add --no-cache bash 

RUN adduser --disabled-password $user
ADD ./deploy /app
ADD ./flag /
WORKDIR /app
RUN pip install -r requirements.txt

RUN chown root:$user /flag
RUN chmod 744 /flag

USER $user
EXPOSE $port

ENTRYPOINT ["python"]
CMD ["app.py"]