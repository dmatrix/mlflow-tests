from random import random, randint
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
import warnings

if __name__ == "__main__":

    warnings.filterwarnings("ignore")
    print(mlflow.__version__)

    local_store_uri = "sqlite:///mlruns.db"
    mlflow.set_tracking_uri(local_store_uri)
    with mlflow.start_run(run_name="LOCAL_REGISTRY") as run:
        params = {"n_estimators": 3, "random_state": 42}
        sk_learn_rfr = RandomForestRegressor(params)

        # Log params using the MLflow sklearn APIs
        mlflow.log_params(params)
        mlflow.log_param("param_1", randint(0, 100))
        mlflow.log_metric("metric_1", random())
        mlflow.log_metric("metric_2", random() + 1)
        mlflow.sklearn.log_model(sk_learn_rfr, artifact_path = "sklearn-model")
