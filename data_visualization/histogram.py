import matplotlib.pyplot as plt
import pandas as pd
import sys

def read_dataset():
    """
    Opens the given dataset and selects the label to plot.
    """
    try:
        dataset = pd.read_csv('../datasets/dataset_train.csv')
    except:
        print("\033[1m\033[91mError. Dataset can't be read.\n\033[0m")
        sys.exit(1)
    label = 'Care of Magical Creatures'
    valid_columns = dataset.select_dtypes(include = 'number').columns
    if len(sys.argv) == 2 and sys.argv[1] in valid_columns:
        label = sys.argv[1]
    elif len(sys.argv) == 2:
        print("\033[1m\033[91mError. {} not in:\n\t{}.\n\033[0m".format(sys.argv[1], valid_columns))
        sys.exit(1)
    elif len(sys.argv) >= 3:
        print("\033[1m\033[91mError. histogram.py does not take more than one argument.\n\033[0m")
        sys.exit(1)
    return dataset, label

def plot_histogram(dataset, label):
    """
    Plots the histogram corresponding to the given label.
    """
    raven = dataset.loc[dataset['Hogwarts House'] == 'Ravenclaw']
    slyth = dataset.loc[dataset['Hogwarts House'] == 'Slytherin']
    gryff = dataset.loc[dataset['Hogwarts House'] == 'Gryffindor']
    huffl = dataset.loc[dataset['Hogwarts House'] == 'Hufflepuff']
    plt.hist(raven.loc[:, label], alpha = 0.65, color = 'cornflowerblue', label = 'Ravenclaw')
    plt.hist(slyth.loc[:, label], alpha = 0.65, color = 'limegreen', label = 'Slytherin')
    plt.hist(gryff.loc[:, label], alpha = 0.65, color = 'firebrick', label = 'Gryffindor')
    plt.hist(huffl.loc[:, label], alpha = 0.65, color = 'yellow', label = 'Hufflepuff')
    plt.xlabel(label)
    plt.ylabel('Number of Students')
    plt.title('HISTOGRAM')
    plt.grid(alpha = 0.7)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    dataset, label = read_dataset()
    plot_histogram(dataset, label)
    sys.exit(0)
