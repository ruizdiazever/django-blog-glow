FROM python:3.10.1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN mkdir /source-app
WORKDIR /source-app
COPY requirements.txt /source-app/
RUN pip install -r requirements.txt


COPY . /source-app/
CMD python manage.py runserver 0.0.0.0:$PORT