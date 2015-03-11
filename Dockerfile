FROM python:2.7.7

WORKDIR src

ADD . src

RUN pip install -r requirements.txt

CMD python app.py

EXPOSE 5000
