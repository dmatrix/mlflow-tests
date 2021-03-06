import warnings
from mlflow.tracking import MlflowClient

if __name__ == "__main__":

    warnings.filterwarnings("ignore")

    def print_experiment_info(experiment):
        print("Name: {}".format(experiment.name))
        print("Experiment Id: {}".format(experiment.experiment_id))
        print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))

    # Create and and delete an experiment
    client = MlflowClient()
    experiment_id = client.create_experiment("New Experiment")
    client.delete_experiment(experiment_id)

    # Examine the deleted experiment details. Deleted experiments
    # are moved to a .trash folder under the artifact URI location top
    # level directory.
    experiment = client.get_experiment(experiment_id)
    print_experiment_info(experiment)
    print("--")

    # Restore the experiment from the .trash folder and fetch its info
    client.restore_experiment(experiment_id)
    experiment = client.get_experiment(experiment_id)
    print_experiment_info(experiment)
