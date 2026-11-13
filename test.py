import dagshub

dagshub.init(repo_owner='mahmoudradwaan98', repo_name='dagshub_s05', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)