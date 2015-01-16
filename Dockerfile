FROM canercandan/python3-base

WORKDIR src

ADD . src

RUN apt-get update && apt-get install -y git

RUN pip install -r requirements.txt

CMD python main.py

EXPOSE 5000
