FROM python:3.6.1

WORKDIR /a2-group42

ADD . /a2-group42

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python","web_app.py"]
