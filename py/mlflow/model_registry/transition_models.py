import sys
import pprint
import mlflow
from mlflow.tracking import MlflowClient
import warnings

if __name__ == "__main__":

    warnings.filterwarnings("ignore")
    print(mlflow.__version__)

    if (len(sys.argv) < 2):
        print("Usage: list of versions to archive for the model")
        sys.exit(1)

    # set the tracking server to be localhost with sqlite as tracking store
    local_registry = "sqlite:///mlruns.db"
    mlflow.set_tracking_uri(local_registry)
    print(f"Running local model registry={local_registry}")
    model_name = "IrisClassifierModel"
    version = int(sys.argv[1])
    #
    # Get model name if not registered, register with model registry
    # on a local host
    #
    client = MlflowClient()
    for version in sys.argv[1:]:
        client.transition_model_version_stage(
            name="IrisClassifierModel",
            version=int(version),
            stage="Production",
            archive_existing_versions=True)
    print("=" * 80)
    [pprint.pprint(dict(mv), indent=4) for mv in client.search_model_versions("name='IrisClassifierModel'")]
