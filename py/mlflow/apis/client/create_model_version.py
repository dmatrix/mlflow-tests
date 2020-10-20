import mlflow.sklearn
from mlflow.tracking import MlflowClient
from sklearn.ensemble import RandomForestRegressor


if __name__ == "__main__":

    mlflow.set_tracking_uri("sqlite:///mlruns.db")
    params = {"n_estimators": 3, "random_state": 42}
    name = "RandomForestRegression"
    rfr = RandomForestRegressor(**params)

    # Log MLflow entities
    with mlflow.start_run() as run:
        mlflow.log_params(params)
        mlflow.sklearn.log_model(rfr, artifact_path="sklearn-model")

    # Register model name in the model registry
    client = MlflowClient()
    client.create_registered_model(name)

    # Create a new version of the rfr model under the registered model name
    desc = "A new version of the model"
    model_uri = "runs:/{}/sklearn-model".format(run.info.run_id)
    mv = client.create_model_version(name, model_uri, run.info.run_id, description=desc)
    print("Name: {}".format(mv.name))
    print("Version: {}".format(mv.version))
    print("Description: {}".format(mv.description))
    print("Status: {}".format(mv.status))
    print("Stage: {}".format(mv.current_stage))
