FROM python:3

ENV workdir /app
RUN mkdir -p $workdir
WORKDIR $workdir

ADD requirements.txt $workdir/requirements.txt

RUN pip install -r requirements.txt
