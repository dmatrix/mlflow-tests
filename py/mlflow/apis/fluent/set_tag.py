#
# Code snippet for https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.set_tag
#
import warnings

import mlflow

if __name__ == "__main__":

    warnings.filterwarnings("ignore")
    print(mlflow.__version__)

    tags = {"engineering": "ML Platform",
            "release.candidate": "RC1",
            "release.version": "2.2.0"}

    # Use Context Manager to create a new run and set tags
    with mlflow.start_run(run_name="My Runs"):
        for key, value in tags.items():
            mlflow.set_tag(key, value)



