from mlflow.tracking import MlflowClient

if __name__ == "__main__":

    def print_run_info(r):
        print("run_id: {}".format(r.info.run_id))
        print("status: {}".format(r.info.status))

    # Create a run, and since this is low-level CRUD operations,
    # this method will create a run. To end the run, you'll have to
    # explicitly terminate it.
    client = MlflowClient()
    run = client.create_run("0")
    print_run_info(run)
    print("--")

    # Terminate the run and fetch updated status. By default,
    # the status is set to "FINISHED." Other values you can
    # set are "KILLED", "FAILED", "RUNNING", or "SCHEDULED".
    client.set_terminated(run.info.run_id, status="KILLED")
    run = client.get_run(run.info.run_id)
    print_run_info(run)
