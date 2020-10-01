from mlflow.tracking import MlflowClient

if __name__ == "__main__":

    def print_run_info(r):
        print("run_id: {}".format(r.info.run_id))
        print("metrics: {}".format(r.data.metrics))
        print("status: {}".format(r.info.status))

    # Create a run without any tags. Since these are low-level CRUD operations,
    # this method will create a run. To end the run, you'll have to
    # explicitly end it.
    client = MlflowClient()
    run = client.create_run("0")
    print_run_info(run)
    print("--")

    # Terminate the run and fetch updated status
    client.set_terminated(run.info.run_id)
    run = client.get_run(run.info.run_id)
    print_run_info(run)
    print("--")

    # Log the metric. Unlike mlflow.log_metric this method
    # does not start a run if one does not exists. It will log
    # the metric for the run id in the backend store
    client.log_metric(run.info.run_id, "m", 1.5)
    run = client.get_run(run.info.run_id)
    print_run_info(run)