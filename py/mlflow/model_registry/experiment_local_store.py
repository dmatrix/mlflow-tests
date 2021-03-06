import os
import shutil
import pprint

from random import random, randint
import mlflow.sklearn
from mlflow import log_metric, log_param, log_artifacts
from sklearn.ensemble import RandomForestRegressor
from mlflow.tracking import MlflowClient
import warnings

if __name__ == "__main__":

    warnings.filterwarnings("ignore")
    print(mlflow.__version__)

    # Set the tracking server to be localhost with sqlite as tracking store
    local_registry = "sqlite:///mlruns.db"
    print(f"Running local model registry={local_registry}")
    model_name="AzureWeatherForecastModel"
    mlflow.set_tracking_uri(local_registry)
    with mlflow.start_run(run_name="LOCAL_REGISTRY") as run:
        params = {"n_estimators": 3, "random_state": 0}
        sk_learn_rfr = RandomForestRegressor(params)

        # Log parameters and metrics using the MLflow API
        mlflow.log_params(params)
        log_param("param_1", randint(0, 100))
        log_metric("metric_1", random())
        log_metric("metric_2", random() + 1)
        log_metric("metric_33", random() + 2)

        # Log and register the model at the same time
        mlflow.sklearn.log_model(
                    sk_model = sk_learn_rfr,
                    artifact_path = "sklearn-model",
                    registered_model_name="AzureWeatherForecastModel")
        if not os.path.exists("outputs"):
            os.makedirs("outputs")
        with open("outputs/test.txt", "w") as f:
            f.write("Looks, like I logged to the local store!")
        log_artifacts("outputs")
        shutil.rmtree('outputs')
        run_id = run.info.run_uuid

    client = MlflowClient()
    #
    # transition model stage to production
    #
    client.transition_model_version_stage(
        name=model_name,
        version=1,
        stage="production")

    # Get a list of all registered models
    print("List of all registered models")
    print("=" * 80)
    [print(pprint.pprint(dict(rm), indent=4)) for rm in client.list_registered_models()]

    # Get a list of specific versions of the named models
    print(f"List of Model = {model_name} and Versions")
    print("=" * 80)
    [pprint.pprint(dict(mv), indent=4) for mv in client.search_model_versions("name='AzureWeatherForecastModel'")]
