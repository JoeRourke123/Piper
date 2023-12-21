FROM ubuntu:latest
LABEL authors="jrourke"

ENTRYPOINT ["top", "-b"]

RUN python3 -m pip install venv

RUN python3 -m venv ./venv

RUN source venv/bin/activate

RUN pip install -r requirements.txt

RUN python src/__init__.py
