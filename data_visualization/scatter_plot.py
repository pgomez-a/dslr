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
    xlabel = 'Astronomy'
    ylabel = 'Defense Against the Dark Arts'
    valid_columns = dataset.select_dtypes(include = 'number').columns
    if len(sys.argv) == 3 and sys.argv[1] in valid_columns and sys.argv[2] in valid_columns:
        xlabel = sys.argv[1]
        ylabel = sys.argv[2]
    elif len(sys.argv) == 3:
        print("\033[1m\033[91mError. [{}, {}] not in:\n\t{}.\n\033[0m".format(sys.argv[1], sys.argv[2], valid_columns))
        sys.exit(1)
    elif len(sys.argv) == 2 or len(sys.argv) >= 4: 
        print("\033[1m\033[91mError. scatter_plot.py can only take two arguments.\n\033[0m")
        sys.exit(1)
    return dataset, xlabel, ylabel

def plot_scatter(dataset, xlabel, ylabel):
    """
    Plots the scatter plot corresponding to the given label.
    """
    raven = dataset.loc[dataset['Hogwarts House'] == 'Ravenclaw']
    slyth = dataset.loc[dataset['Hogwarts House'] == 'Slytherin']
    gryff = dataset.loc[dataset['Hogwarts House'] == 'Gryffindor']
    huffl = dataset.loc[dataset['Hogwarts House'] == 'Hufflepuff']
    plt.scatter(raven.loc[:, xlabel], raven.loc[:, ylabel], alpha = 0.65, color = 'cornflowerblue', label = 'Ravenclaw')
    plt.scatter(slyth.loc[:, xlabel], slyth.loc[:, ylabel], alpha = 0.65, color = 'limegreen', label = 'Slytherin')
    plt.scatter(gryff.loc[:, xlabel], gryff.loc[:, ylabel], alpha = 0.65, color = 'firebrick', label = 'Gryffindor')
    plt.scatter(huffl.loc[:, xlabel], huffl.loc[:, ylabel], alpha = 0.65, color = 'yellow', label = 'Hufflepuff')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title('SCATTER PLOT')
    plt.grid(alpha = 0.7)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    dataset, xlabel, ylabel = read_dataset()
    plot_scatter(dataset, xlabel, ylabel)
    sys.exit(0)
