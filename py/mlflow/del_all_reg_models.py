import sys
import pprint
import mlflow
from mlflow.tracking import MlflowClient
import warnings

if __name__ == "__main__":

    warnings.filterwarnings("ignore")
    print(mlflow.__version__)

    # set the tracking server to be Databricks Community Edition
    # set the experiment name; if name does not exist, MLflow will
    # create one for you
    local_registry = "sqlite:///mlruns.db"
    mlflow.set_tracking_uri(local_registry)
    print(f"Running local model registry={local_registry}")
    model_name = "sk-learn-random-forest-reg-model"
    #
    # Get model name if not regisered, register with model registry
    # on a local host
    #
    client = MlflowClient()
    client.delete_registered_model("sk-learn-random-forest-reg-model")
    print("=" * 80)
    [pprint.pprint(dict(mv), indent=4) for mv in client.search_model_versions("name='sk-learn-random-forest-reg-model'")]