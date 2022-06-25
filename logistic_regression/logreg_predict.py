import pandas as pd
import numpy as np
import warnings
import math
import sys

def read_dataset():
    """
    Opens the given dataset.
    """
    if len(sys.argv) != 3:
        print("\033[1m\033[91mError. logreg_train.py needs a dataset and a thetas file.\n\033[0m")
        sys.exit(1)
    try:
        print("\033[1mReading dataset...\033[0m")
        dataset = pd.read_csv(sys.argv[1]).iloc[:, 1:]
    except:
        print("\033[1m\033[91mError. {} can't be read.\n\033[0m".format(sys.argv[1]))
        sys.exit(1)
    try:
        print("\033[1mReading weights...\033[0m")
        weights = pd.read_csv(sys.argv[2]).iloc[:, 1:]
    except:
        print("\033[1m\033[91mError. {} can't be read.\n\033[0m".format(sys.argv[2]))
        sys.exit(1)
    return dataset, weights

def normalize(X, mean_val, max_val, min_val):
    """
    Normalizes the given value.
    """
    X = X.transpose()
    for pos in range(1, X.shape[0]):
        X[pos] = (X[pos] - mean_val[pos]) / (max_val[pos] - min_val[pos])
    return X.transpose()

def get_logreg_values(dataset, weights):
    """
    Gets the dependent and independent variables.
    Gets the theta array with the according shape.
    """
    print("\033[1mGetting independent variables...\033[0m")
    mean_val = np.array(weights.loc[:, 'Mean']).reshape((1, -1))[0]
    max_val = np.array(weights.loc[:, 'Max']).reshape((1, -1))[0]
    min_val = np.array(weights.loc[:, 'Min']).reshape((1, -1))[0]
    X = np.array(dataset.select_dtypes(include = 'number').iloc[:, 1:])
    X = np.insert(X, 0, 1, 1)
    X[np.isnan(X)] = 0.
    return normalize(X, mean_val, max_val, min_val)

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

def get_label_predictions(X, raven_theta, slyth_theta, gryff_theta, huffl_theta):
    """
    Computes the four predictions for the given thetas and creates and (n x 4) matrix.
    """
    print("\033[1mPredicting students' house...\033[0m")
    raven_pred = predict(X, raven_theta)
    slyth_pred = predict(X, slyth_theta)
    gryff_pred = predict(X, gryff_theta)
    huffl_pred = predict(X, huffl_theta)
    predictions = np.append(raven_pred, slyth_pred, 1)
    predictions = np.append(predictions, gryff_pred, 1)
    predictions = np.append(predictions, huffl_pred, 1)
    return predictions

def predict_house(predictions):
    """
    Predicts the student's house according to the highest probability.
    """
    labels = ['Ravenclaw', 'Slytherin', 'Gryffindor', 'Hufflepuff']
    houses = pd.DataFrame([], dtype = object)
    index = 0
    for student in predictions:
        house = labels[np.where(student == max(student))[0][0]]
        house = pd.Series([index, house])
        houses = houses.append(house, ignore_index = True)
        index += 1
    houses[0] = houses[0].astype(int)
    houses.columns = ['Index', 'Hogwarts House']
    houses.to_csv('houses.csv', index = False)
    print("\033[1m\nDone! houses.csv file has been created and saved.\n\033[0m")

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    dataset, weights = read_dataset()
    raven_theta = np.array(weights.loc[:, 'Raven']).reshape((-1, 1))
    slyth_theta = np.array(weights.loc[:, 'Slyth']).reshape((-1, 1))
    gryff_theta = np.array(weights.loc[:, 'Gryff']).reshape((-1, 1))
    huffl_theta = np.array(weights.loc[:, 'Huffl']).reshape((-1, 1))
    X = get_logreg_values(dataset, weights)
    predictions = get_label_predictions(X, raven_theta, slyth_theta, gryff_theta, huffl_theta)
    predict_house(predictions)
    sys.exit(0)
