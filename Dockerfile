FROM python:3.10-slim

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y make
RUN apt-get install -y binutils

RUN pip install poetry

COPY ./ /PROJECT
WORKDIR /PROJECT
RUN make install-in-linux
RUN cp dist/obfuscate /bin/obfuscate
RUN rm -rf *
