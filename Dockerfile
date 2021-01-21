FROM ubuntu

WORKDIR /catalog

COPY . .

RUN apt-get update && apt-get install -y python3-pip\
    && pip3 install -r requirements.txt

ENV FLASK_APP=crud.py

EXPOSE 5000

CMD [ "flask", "run", "-h", "0.0.0.0"]

