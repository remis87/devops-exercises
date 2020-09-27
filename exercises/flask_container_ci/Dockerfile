# pull official base image
FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /usr/src/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r requirements.txt

RUN pip install gunicorn

# copy project
COPY ./ /usr/src/

EXPOSE 5000
WORKDIR /usr/src/app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:application"]
