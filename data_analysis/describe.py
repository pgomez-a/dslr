import pandas as pd
import numpy as np
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

def get_count(dataset):
    """
    Computes the count value of each column for the given dataset.
    """
    count_list = np.array([]) 
    for label in dataset:
        count_list = np.append(count_list, dataset[label].size - dataset[label].isnull().sum())
    return count_list

def get_mean(dataset, count):
    """
    Compute the mean value of each column for the given dataset.
    """
    mean_list = np.array([])
    for label in dataset:
        mean_list = np.append(mean_list, dataset[label].sum())
    return mean_list / count

def get_std(dataset, count, mean):
    """
    Compute the std value of each column for the given dataset.
    """
    std_list = np.array([])
    pos = 0
    for label in dataset:
        std_list = np.append(std_list, ((dataset[label] - mean[pos]) ** 2).sum())
        pos += 1
    return np.sqrt(std_list / (count - 1))

def get_min(dataset):
    """
    Finds the min value of each column for the given dataset.
    """
    min_list = np.array([])
    for label in dataset:
        min_value = dataset[label][0]
        for value in dataset[label]:
            if value < min_value:
                min_value = value
        min_list = np.append(min_list, min_value)
    return min_list

def get_max(dataset):
    """
    Finds the max value of each column for the given dataset.
    """
    max_list = np.array([])
    for label in dataset:
        max_value = dataset[label][0]
        for value in dataset[label]:
            if value > max_value:
                max_value = value
        max_list = np.append(max_list, max_value)
    return max_list

def get_percentile(percentile, dataset, count):
    """
    Computes the specified percentile of each column for the given dataset.
    """
    percentile_list = np.array([])
    pos = 0
    for label in dataset:
        values = dataset[label].copy()
        values = pd.Series(values.sort_values().values)
        percentile_pos = count[pos] * percentile
        percentile_floor = np.floor(percentile_pos)
        percentile_ceil = np.ceil(percentile_pos)
        if percentile_ceil - percentile_floor == 0:
            valueOne = values[int(percentile_floor) - 1]
            valueTwo = values[int(percentile_ceil)]
            percentile_list = np.append(percentile_list, (valueOne + valueTwo) / 2)
        else:
            percentile_list = np.append(percentile_list, values[int(percentile_ceil) - 1])
        pos += 1
    return percentile_list

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("\033[1m\033[91mError. Dataset to open doesn't specified.\n\033[0m")
        sys.exit(1)
    dataset = read_dataset(sys.argv[1])
    dataset = dataset.select_dtypes(include = 'number')
    data_count = get_count(dataset)
    data_mean = get_mean(dataset, data_count)
    data_std = get_std(dataset, data_count, data_mean)
    data_min = get_min(dataset)
    data_max = get_max(dataset)
    data_p25 = get_percentile(0.25, dataset, data_count)
    data_p50 = get_percentile(0.5, dataset, data_count)
    data_p75 = get_percentile(0.75, dataset, data_count)
    describe_values = [data_count, data_mean, data_std, data_min, data_p25, data_p50, data_p75, data_max]
    describe_index = ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max']
    describe = pd.DataFrame(describe_values, index = describe_index, columns = dataset.columns)
    print(describe)
    sys.exit(0)
