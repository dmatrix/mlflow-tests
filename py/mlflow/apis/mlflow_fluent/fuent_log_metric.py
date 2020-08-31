#
# Code snippet for https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.log_metric
#
import warnings

import mlflow

if __name__ == "__main__":

    warnings.filterwarnings("ignore")
    print(mlflow.__version__)

    # Create a run if one is not active and log two metrics
    mlflow.start_run()
    mlflow.log_metric("mse", 2500.00)
    mlflow.log_metric("rsme", 50.00)
    mlflow.end_run()

    # Or you Context Manager create a new run
    with mlflow.start_run(run_name="My Runs"):
        mlflow.log_metric("mse", 2500.00)
        mlflow.log_metric("rsme", 50.00)
