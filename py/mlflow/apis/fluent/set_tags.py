#
# Code snippet for https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.set_tags
#
import warnings

import mlflow

if __name__ == "__main__":

    warnings.filterwarnings("ignore")
    print(mlflow.__version__)

    tags = {"engineering": "ML Platform",
            "release.candidate": "RC1",
            "release.version": "2.2.0"}

    # Set a batch of tags
    with mlflow.start_run(run_name="My Runs"):
        mlflow.set_tags(tags)



