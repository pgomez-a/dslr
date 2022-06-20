import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import sys

def read_dataset():
    """
    Opens the given dataset.
    """
    if len(sys.argv) != 2:
        print("\033[1m\033[91mError. logreg_train.py needs a dataset to read.\n\033[0m")
        sys.exit(1)
    try:
        dataset = pd.read_csv(sys.argv[1])
    except:
        print("\033[1m\033[91mError. {} can't be read.\n\033[0m".format(sys.argv[1]))
        sys.exit(1)
    return dataset

def get_logreg_values(dataset):
    """
    Gets the dependent and independent variables.
    Gets the theta array with the according shape.
    """
    Y = np.array(dataset.loc[:, 'Hogwarts House']).reshape((-1, 1))
    X = np.array(dataset.select_dtypes(include = 'number').iloc[:, 1:])
    X = np.insert(X, 0, 1, 1)
    X[np.isnan(X)] = 0.
    theta = np.zeros([1, X.shape[1]]).reshape((-1, 1))
    return X, Y, theta

def progress_bar(iters, label):
    """
    Shows a progress bar to see the evolution of the model.
    """
    bar = ""
    for it in range(iters):
        perc = (100 * it) / iters
        if perc % 2 == 0:
            bar += "="
        print("\033[1m[{}][{: <51}] {}/{}  {:.0f}%\033[0m".format(label, bar + ">", it + 1, iters, perc), end = "\r")
        yield it
    print()

def sigmoid(X):
    """
    Computes the sigmoid value for the given parameter.
    """
    return 1 / (1 + math.e ** -X)

def predict(X, theta):
    """
    Predicts the desired label for the given parameters.
    """
    return sigmoid(np.matmul(X, theta))

def loss(X, theta, Y, label):
    """
    Computes the loss for the given parameters.
    """
    Y_hat = predict(X, theta)
    Y_hat[Y_hat == 0.] += 1e-15
    Y_hat[Y_hat == 1.] -= 1e-15
    Y[Y != label] = 0.
    Y[Y == label] = 1.
    return -sum(Y * np.log(Y_hat) + (1 - Y) * np.log(1 - Y_hat)) / Y.size

def gradient(X, theta, Y, label):
    """
    Computes a gradient descent for the given values.
    """
    Y_hat = predict(X, theta)
    cost = (Y_hat - Y).astype(float)
    cost[np.isnan(cost)] = 1.
    return  np.matmul(X.transpose(), cost) / Y.size

def train(X, theta, Y, label):
    """
    Trains the model adjusted to the desired label for the given parameters.
    """
    alpha = 0.01
    max_iter = 10000
    Y[Y != label] = 0.
    Y[Y == label] = 1.
    for i in progress_bar(max_iter, label):
        theta -= alpha * gradient(X, theta, Y, label)
    return theta

def store_in_file(file, theta):
    """
    Stores in save_theta the given label_theta.
    """
    for elem in theta:
        file.write(str(elem[0]) + ' ')
    file.write('\n')

if __name__ == '__main__':
    dataset = read_dataset()
    save_theta = open('.theta', 'w')
    X, Y, theta = get_logreg_values(dataset)
    raven_theta = train(X, np.copy(theta), np.copy(Y), 'Ravenclaw') 
    slyth_theta = train(X, np.copy(theta), np.copy(Y), 'Slytherin')
    gryff_theta = train(X, np.copy(theta), np.copy(Y), 'Gryffindor')
    huffl_theta = train(X, np.copy(theta), np.copy(Y), 'Hufflepuff')
    store_in_file(save_theta, raven_theta)
    store_in_file(save_theta, slyth_theta)
    store_in_file(save_theta, gryff_theta)
    store_in_file(save_theta, huffl_theta)
    sys.exit(0)
