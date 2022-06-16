import matplotlib.pyplot as plt
import pandas as pd
import sys

def read_dataset(data_file):
    """
    Opens the given dataset.
    """
    try:
        dataset = pd.read_csv(data_file)
        return dataset
    except:
        print("\033[1m\033[91mError. {} can't be read.\n\033[0m".format(data_file))
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\033[1m\033[91mError. Dataset to open doesn't specified.\n\033[0m")
        sys.exit(1)
    dataset = read_dataset(sys.argv[1])
    numeric_dataset = dataset.select_dtypes(include = 'number')
    figure, axis = plt.subplots(2, 7)
    y_axis = 0
    x_axis = 0
    for label in numeric_dataset:
        raven = dataset.loc[dataset['Hogwarts House'] == 'Ravenclaw']
        slyth = dataset.loc[dataset['Hogwarts House'] == 'Slytherin']
        gryff = dataset.loc[dataset['Hogwarts House'] == 'Gryffindor']
        huffl= dataset.loc[dataset['Hogwarts House'] == 'Hufflepuff']
        axis[y_axis, x_axis].hist(raven.loc[:, label], alpha = 0.75, color = 'cornflowerblue')
        axis[y_axis, x_axis].hist(slyth.loc[:, label], alpha = 0.75, color = 'limegreen')
        axis[y_axis, x_axis].hist(gryff.loc[:, label], alpha = 0.75, color = 'firebrick')
        axis[y_axis, x_axis].hist(huffl.loc[:, label], alpha = 0.75, color = 'yellow')
        axis[y_axis, x_axis].set_xlabel(label)
        if x_axis == 0:
            axis[y_axis, x_axis].set_ylabel('Number of students')
        x_axis += 1
        if x_axis == 7:
            y_axis += 1
            x_axis = 0
    figure.legend(labels = ['Ravenclaw', 'Slytherin', 'Gryffindor', 'Hufflepuff'])
    plt.show()
    sys.exit(0)
