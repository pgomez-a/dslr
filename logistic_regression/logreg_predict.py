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

def get_theta_values(label):
    """
    Gets the theta array for the corresponding label.
    """
    try:
        with open('.theta', 'r') as f:
            for i in range(label):
                data = f.readline().split()
            data = np.array(data).astype(float)
            return data.reshape((-1, 1))
    except:
        print("\033[1m\033[91mError. .theta file can't be read.\n\033[0m")
        sys.exit(1)


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

if __name__ == '__main__':
    dataset = read_dataset()
    X, Y, theta = get_logreg_values(dataset)
    raven_theta = get_theta_values(1) 
    slyth_theta = get_theta_values(2)
    gryff_theta = get_theta_values(3)
    huffl_theta = get_theta_values(4)
    print(predict(X, huffl_theta)[:10])
    sys.exit(0)
