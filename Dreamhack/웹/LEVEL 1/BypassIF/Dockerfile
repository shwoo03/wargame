FROM python:3.11-alpine@sha256:af8fef83397b3886ed93d2c81bf3b4e70d39c0789c1c6feb1ecb86ca9bc42a0a

# ENV
ENV APP_USER chall
ENV APP_PORT 8000

# SET challenges
RUN adduser --disabled-password $APP_USER

RUN mkdir /app
ADD ./requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
ADD ./ /app

RUN chown $APP_USER:$APP_USER /app
RUN chmod 444 /app/flag.txt

USER $APP_USER
EXPOSE $APP_PORT

ENTRYPOINT ["python"]
CMD ["app.py"]