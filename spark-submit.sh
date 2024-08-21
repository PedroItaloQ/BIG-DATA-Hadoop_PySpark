Script para enviar o job Spark ao cluster Hadoop.

```bash

spark-submit \
  --master yarn \
  --deploy-mode cluster \
  --num-executors 4 \
  --executor-memory 2g \
  --driver-memory 2g \
  scripts/bigdata_pipeline.py