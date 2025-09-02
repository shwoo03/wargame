FROM python:3.7-alpine

# ENV
ENV APP_USER dreamhack
ENV APP_PORT 8000

# SET challenges
RUN adduser --disabled-password $APP_USER
ADD ./deploy /app
WORKDIR /app

# RUN pip install flask
RUN pip install -r requirements.txt
RUN chown $APP_USER:$APP_USER /app

# RUN
USER $APP_USER
EXPOSE $APP_PORT

ENTRYPOINT ["python"]
CMD ["app.py"]
