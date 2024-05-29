# image docker of python
FROM python:3.9-slim-buster

LABEL maintainer="hrdip.2018@gmail.com"

# write byte code in the console
ENV PYTHONDONTWRITEBYTECODE=1
# show activity in the terminal without buffer
ENV PYTHONUNBUFFERED=1

# after make image we work in this directory( keeping in "app" folder inside of python image we build now)
WORKDIR /usr/src/app

# copy requirements.txt file to the working directory (app)
COPY ./requirements.txt .


RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# this code we are written copy to the working directory
COPY ./core /app
