FROM python:3

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN apt-get update && apt-get install -y vim
RUN pip install -r requirements.txt

COPY . /

ENTRYPOINT [ "python3" ]

CMD [ "app1.py" ]
