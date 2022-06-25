import pandas as pd
import numpy as np
import warnings
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
    return Y, X, theta

def progress_bar(iters, label):
    """
    Shows a progress bar to see the evolution of the model.
    """
    bar = ""
    for it in range(iters):
        perc = (100 * it) / iters
        if perc % 2 == 0:
            bar += "="
        print("\033[1m[{:10}][{: <51}]".format(label, bar + ">"), end = " ")
        print("{}/{}  {:.0f}%\033[0m".format(it + 1, iters, perc), end = "\r")
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

def loss(Y, Y_hat, theta, label):
    """
    Computes the loss for the given parameters.
    """
    Y[Y != label] = 0.
    Y[Y == label] = 1.
    Y_hat[Y_hat == 0.] += 1e-15
    Y_hat[Y_hat == 1.] -= 1e-15
    return -sum(Y * np.log(Y_hat) + (1 - Y) * np.log(1 - Y_hat)) / Y.size

def train(Y, X, theta, label):
    """
    Trains the model adjusted to the desired label for the given parameters.
    """
    alpha = 0.01
    max_iter = 10000
    Y[Y != label] = 0.
    Y[Y == label] = 1.
    for i in progress_bar(max_iter, label):
        Y_hat = predict(X, theta)
        cost = (Y_hat - Y).astype(float)
        tmp_theta = np.matmul(X.transpose(), cost) / Y.size
        theta -= (alpha * tmp_theta)
    return theta

def store_in_file(file, theta):
    """
    Stores in save_theta the given label_theta.
    """
    for elem in theta:
        file.write(str(elem[0]) + ' ')
    file.write('\n')

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    dataset = read_dataset()
    save_theta = open('weights', 'w')
    Y, X, theta = get_logreg_values(dataset)
    raven_theta = train(np.copy(Y), X, np.copy(theta), 'Ravenclaw') 
    slyth_theta = train(np.copy(Y), X, np.copy(theta), 'Slytherin')
    gryff_theta = train(np.copy(Y), X, np.copy(theta), 'Gryffindor')
    huffl_theta = train(np.copy(Y), X, np.copy(theta), 'Hufflepuff')
    store_in_file(save_theta, raven_theta)
    store_in_file(save_theta, slyth_theta)
    store_in_file(save_theta, gryff_theta)
    store_in_file(save_theta, huffl_theta)
    sys.exit(0)
