


FROM python:3.10.9

RUN apt-get update --fix-missing && \
    apt-get install --reinstall -y build-essential && \
    apt-get install -y cmake && \
    apt-get install -y cron && \
    apt-get install vim -y

ENV INSTALL_PATH /reccomender_frontend
RUN mkdir -p INSTALL_PATH
WORKDIR $INSTALL_PATH
RUN export PYTHONPATH=$(pwd):$PYTHONPATH

RUN apt-get install -y uwsgi-plugin-python3
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
