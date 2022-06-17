import matplotlib.pyplot as plt
import pandas as pd
import sys

def read_dataset():
    """
    Opens the given dataset and selects the label to plot.
    """
    if len(sys.argv) != 1:
        print("\033[1m\033[91mError. pair_plot.py does not take any argument.\n\033[0m")
        sys.exit(1)
    try:
        dataset = pd.read_csv('../datasets/dataset_train.csv')
    except:
        print("\033[1m\033[91mError. Dataset can't be read.\n\033[0m")
        sys.exit(1)
    return dataset

def plot_histogram(subplot, dataset, label):
    """
    Plots the histogram corresponding to the given label.
    """
    raven = dataset.loc[dataset['Hogwarts House'] == 'Ravenclaw']
    slyth = dataset.loc[dataset['Hogwarts House'] == 'Slytherin']
    gryff = dataset.loc[dataset['Hogwarts House'] == 'Gryffindor']
    huffl = dataset.loc[dataset['Hogwarts House'] == 'Hufflepuff']
    subplot.hist(raven.loc[:, label], alpha = 0.65, color = 'cornflowerblue', label = 'Ravenclaw')
    subplot.hist(slyth.loc[:, label], alpha = 0.65, color = 'limegreen', label = 'Slytherin')
    subplot.hist(gryff.loc[:, label], alpha = 0.65, color = 'firebrick', label = 'Gryffindor')
    subplot.hist(huffl.loc[:, label], alpha = 0.65, color = 'yellow', label = 'Hufflepuff')

def plot_scatter(subplot, dataset, xlabel, ylabel):
    """
    Plots the scatter plot corresponding to the given label.
    """
    raven = dataset.loc[dataset['Hogwarts House'] == 'Ravenclaw']
    slyth = dataset.loc[dataset['Hogwarts House'] == 'Slytherin']
    gryff = dataset.loc[dataset['Hogwarts House'] == 'Gryffindor']
    huffl = dataset.loc[dataset['Hogwarts House'] == 'Hufflepuff']
    subplot.scatter(raven.loc[:, xlabel], raven.loc[:, ylabel], alpha = 0.65, s = 0.7, color = 'cornflowerblue', label = 'Ravenclaw')
    subplot.scatter(slyth.loc[:, xlabel], slyth.loc[:, ylabel], alpha = 0.65, s = 0.7, color = 'limegreen', label = 'Slytherin')
    subplot.scatter(gryff.loc[:, xlabel], gryff.loc[:, ylabel], alpha = 0.65, s = 0.7, color = 'firebrick', label = 'Gryffindor')
    subplot.scatter(huffl.loc[:, xlabel], huffl.loc[:, ylabel], alpha = 0.65, s = 0.7, color = 'yellow', label = 'Hufflepuff')

if __name__ == '__main__':
    dataset = read_dataset()
    num_dataset = dataset.select_dtypes(include = 'number')
    fig, axis = plt.subplots(num_dataset.shape[1] - 1, num_dataset.shape[1] - 1)
    y_pos = 0
    for y_label in num_dataset.iloc[:, 1:]:
        x_pos = 0
        for x_label in num_dataset.iloc[:, 1:]:
            if y_label == x_label:
                plot_histogram(axis[y_pos, x_pos], dataset, y_label)
            else:
                plot_scatter(axis[y_pos, x_pos], dataset, x_label, y_label)
            if x_pos == 0:
                axis[y_pos, x_pos].set_ylabel(y_label.replace(' ', '\n'))
            else:
                axis[y_pos, x_pos].set_yticks([])
            if y_pos == num_dataset.shape[1] - 2:
                axis[y_pos, x_pos].set_xlabel(x_label.replace(' ', '\n'))
            else:
                axis[y_pos, x_pos].set_xticks([])
            x_pos += 1
        y_pos += 1
    plt.legend(['Ravenclaw', 'Slytherin', 'Gryffindor', 'Hufflepuff'])
    plt.show()
    sys.exit(0)
