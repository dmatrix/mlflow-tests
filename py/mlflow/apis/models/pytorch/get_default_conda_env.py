import warnings
import os

import numpy as np
import torch
import mlflow.pytorch


class LinearNNModel(torch.nn.Module):

    def __init__(self):
       super(LinearNNModel, self).__init__()
       self.linear = torch.nn.Linear(1, 1)  # One in and one out

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred


if __name__ == '__main__':
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
    warnings.filterwarnings("ignore")
    print(mlflow.__version__)

    def gen_data():

        # Example linear model modified to use y = 2x
        # from https://github.com/hunkim/PyTorchZeroToAll/blob/master/05_linear_regression.py
        # X training data, y labels
        X = torch.arange(1.0, 25.0).view(-1, 1)
        y = torch.from_numpy(np.array([x * 2 for x in X])).view(-1, 1)
        return X, y

    # Initialize our model
    model = LinearNNModel()
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

    # Training loop
    epochs = 250
    X, y = gen_data()
    for epoch in range(epochs):

        # Forward pass: Compute predicted y by passing X to the model
        y_pred = model(X)

        # Compute the loss
        loss = criterion(y_pred, y)

        # Zero gradients, perform a backward pass, and update the weights.
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 50 == 0:
            print('Epoch: {}/{}, loss: {:.4f}'.format(epoch + 1., epochs, loss.data.item()))

    # Log PyTorch model
    with mlflow.start_run() as run:
        mlflow.pytorch.log_model(model, "model")

    # Fetch the associated conda environment
    print("run_id: {}".format(run.info.run_id))
    env = mlflow.pytorch.get_default_conda_env()
    print("conda environment: {}".format(env))



