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

def loss(Y, Y_hat, theta, lambda_, label):
    """
    Computes the loss for the given parameters.
    """
    Y[Y != label] = 0.
    Y[Y == label] = 1.
    Y_hat[Y_hat == 0.] += 1e-15
    Y_hat[Y_hat == 1.] -= 1e-15
    l2_theta = np.copy(theta)
    l2_theta[0][0] = 0.
    non_reg_cost = -sum(Y * np.log(Y_hat) + (1 - Y) * np.log(1 - Y_hat)) / Y.size
    return non_reg_cost + (lambda_ * np.matmul(l2_theta.transpose(), l2_theta)) / (2 * Y.size)

def gradient(Y, X, theta, lambda_):
    """
    Computes a gradient descent for the given values.
    """
    Y_hat = predict(X, theta)
    cost = (Y_hat - Y).astype(float)
    l2_theta = np.copy(theta)
    l2_theta[0][0] = 0.
    non_reg_grad = np.matmul(X.transpose(), cost)
    return (non_reg_grad + (lambda_ * l2_theta)) / Y.size

def train(Y, X, theta, lambda_, label):
    """
    Trains the model adjusted to the desired label for the given parameters.
    """
    alpha = 0.0001
    max_iter = 50000
    Y[Y != label] = 0.
    Y[Y == label] = 1.
    for i in progress_bar(max_iter, label):
        tmp_theta = gradient(Y, X, theta, lambda_)
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
    save_theta = open('.theta', 'w')
    Y, X, theta = get_logreg_values(dataset)
    raven_theta = train(np.copy(Y), X, np.copy(theta), 0.1, 'Ravenclaw') 
    slyth_theta = train(np.copy(Y), X, np.copy(theta), 0.1, 'Slytherin')
    gryff_theta = train(np.copy(Y), X, np.copy(theta), 0.1, 'Gryffindor')
    huffl_theta = train(np.copy(Y), X, np.copy(theta), 0.1, 'Hufflepuff')
    store_in_file(save_theta, raven_theta)
    store_in_file(save_theta, slyth_theta)
    store_in_file(save_theta, gryff_theta)
    store_in_file(save_theta, huffl_theta)
    sys.exit(0)
