# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt


COPY . /code/
CMD python manage.py runserver 0.0.0.0:$PORT