FROM python:3.11

RUN  /usr/local/bin/python -m pip install --upgrade pip

RUN pip3 install pyyaml==5.3.1 glob2==0.7

RUN apt-get update && apt-get install -y dos2unix

WORKDIR /src

RUN ls -ls

COPY Scripts /src/Scripts

RUN find /src/Scripts -type f -print0 | xargs -0 dos2unix

RUN chmod +x ./Scripts/buildDocs.sh

CMD ["./Scripts/buildDocs.sh"]