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
        print("\033[1m\033[91mi\rError. logreg_train.py needs a dataset and a thetas file.\n\033[0m")
        sys.exit(1)
    try:
        print("\033[1mReading dataset...\033[0m", end = "")
        dataset = pd.read_csv(sys.argv[1])
    except:
        print("\033[1m\033[91m\rError. {} can't be read.\n\033[0m".format(sys.argv[1]))
        sys.exit(1)
    return dataset

def get_logreg_values(dataset):
    """
    Gets the dependent and independent variables.
    Gets the theta array with the according shape.
    """
    print("\033[1m\rGetting independent variables...\033[0m", end = "")
    X = np.array(dataset.select_dtypes(include = 'number').iloc[:, 2:])
    X = np.insert(X, 0, 1, 1)
    X[np.isnan(X)] = 0.
    theta = np.zeros([1, X.shape[1]]).reshape((-1, 1))
    return X, theta

def get_theta_values(label):
    """
    Gets the theta array for the corresponding label.
    """
    try:
        with open(sys.argv[2], 'r') as f:
            print("\033[1m\rGetting {} file...\033[0m".format(sys.argv[2]), end = "")
            for i in range(label):
                data = f.readline().split()
            data = np.array(data).astype(float)
            return data.reshape((-1, 1))
    except:
        print("\033[1m\033[91m\rError. {} file can't be read.\n\033[0m".format(sys.argv[2]))
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

def get_label_predictions(X, raven_theta, slyth_theta, gryff_theta, huffl_theta):
    """
    Computes the four predictions for the given thetas and creates and (n x 4) matrix.
    """
    print("\033[1m\rPredicting students' house...\033[0m", end = "")
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
    print("\033[1m\rDone! houses.csv file has been created and saved.\n\033[0m")

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    dataset = read_dataset()
    X, theta = get_logreg_values(dataset)
    raven_theta = get_theta_values(1) 
    slyth_theta = get_theta_values(2)
    gryff_theta = get_theta_values(3)
    huffl_theta = get_theta_values(4)
    predictions = get_label_predictions(X, raven_theta, slyth_theta, gryff_theta, huffl_theta)
    predict_house(predictions)
    sys.exit(0)
