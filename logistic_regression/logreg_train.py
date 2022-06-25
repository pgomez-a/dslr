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
    X[np.isnan(X)] = 0.
    X = np.insert(X, 0, 1, 1)
    theta = np.zeros([1, X.shape[1]]).reshape((-1, 1))
    return Y, X, theta

def normalize(X):
    """
    Normalizes the given value.
    """
    X = X.transpose()
    for pos in range(1, X.shape[0]):
        X[pos] = (X[pos] - X[pos].mean()) / (max(X[pos]) - min(X[pos]))
    return X.transpose()

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
    X = normalize(X)
    for i in progress_bar(max_iter, label):
        Y_hat = predict(X, theta)
        cost = (Y_hat - Y).astype(float)
        tmp_theta = np.matmul(X.transpose(), cost) / Y.size
        theta -= (alpha * tmp_theta)
    return theta

def store_in_file(X, raven_theta, slyth_theta, gryff_theta, huffl_theta):
    """
    Stores in save_theta the given label_theta.
    """
    mean_val = list()
    max_val = list()
    min_val = list()
    for feature in X.transpose():
        mean_val.append(feature.mean())
        max_val.append(max(feature))
        min_val.append(min(feature))
    weights = pd.DataFrame([], dtype = object)
    weights.insert(0, 'Raven', raven_theta.transpose()[0])
    weights.insert(1, 'Slyth', slyth_theta.transpose()[0])
    weights.insert(2, 'Gryff', gryff_theta.transpose()[0])
    weights.insert(3, 'Huffl', huffl_theta.transpose()[0])
    weights.insert(4, 'Mean', mean_val)
    weights.insert(5, 'Max', max_val)
    weights.insert(6, 'Min', min_val)
    weights.to_csv('weights.csv')
    print("\033[1m\nDone! weights.csv file has been created and saved.\n\033[0m")

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    dataset = read_dataset()
    Y, X, theta = get_logreg_values(dataset)
    raven_theta = train(np.copy(Y), np.copy(X), np.copy(theta), 'Ravenclaw') 
    slyth_theta = train(np.copy(Y), np.copy(X), np.copy(theta), 'Slytherin')
    gryff_theta = train(np.copy(Y), np.copy(X), np.copy(theta), 'Gryffindor')
    huffl_theta = train(np.copy(Y), np.copy(X), np.copy(theta), 'Hufflepuff')
    store_in_file(X, raven_theta, slyth_theta, gryff_theta, huffl_theta)
    sys.exit(0)
