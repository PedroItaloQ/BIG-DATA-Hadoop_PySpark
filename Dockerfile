FROM openjdk:8-jdk-slim

RUN apt-get update && apt-get install -y python3 python3-pip

COPY env/requirements.txt .
RUN pip3 install -r requirements.txt

ENV HADOOP_HOME=/usr/local/hadoop
ENV SPARK_HOME=/usr/local/spark
ENV PATH=$PATH:$HADOOP_HOME/bin:$SPARK_HOME/bin

COPY . /app
WORKDIR /app

CMD ["spark-submit", "scripts/bigdata_pipeline.py"]