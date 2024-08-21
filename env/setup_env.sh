pip install -r env/requirements.txt

export HADOOP_HOME=/usr/local/hadoop
export SPARK_HOME=/usr/local/spark
export PATH=$PATH:$HADOOP_HOME/bin:$SPARK_HOME/bin

echo "Ambiente configurado com sucesso!"