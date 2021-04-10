FROM ubuntu:latest


RUN apt update && \
    apt install python3 -y

RUN useradd pyserver

USER pyserver

WORKDIR /home/pyserver
COPY server1.py  quotes.txt ./
EXPOSE 8000

CMD ["python3", "server1.py"]

