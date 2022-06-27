from sklearn.metrics import accuracy_score
import pandas as pd

truth_dataset = pd.read_csv('../datasets/dataset_truth.csv').loc[:, 'Hogwarts House']
predict_dataset = pd.read_csv('./houses.csv').loc[:, 'Hogwarts House']

print("The accuracy is: {}%".format(accuracy_score(truth_dataset, predict_dataset) * 100))
