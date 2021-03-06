import pandas as pd
import numpy as np
import sys

def read_dataset():
    """
    Opens the given dataset.
    """
    if len(sys.argv) != 1:
        print("\033[1m\033[91mError. describe.py does not take any argument.\n\033[0m")
        sys.exit(1)
    try:
        dataset = pd.read_csv('../datasets/dataset_train.csv')
    except:
        print("\033[1m\033[91mError. Dataset can't be read.\n\033[0m")
        sys.exit(1)
    return dataset

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

def get_var(dataset, count, mean):
    """
    Computes the var value of each column for the given dataset.
    """
    var_list = np.array([])
    pos = 0
    for label in dataset:
        var_list = np.append(var_list, ((dataset[label] - mean[pos]) ** 2).sum())
        pos += 1
    return var_list / (count - 1)

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

def get_cof(std, mean):
    """
    Computes the coefficient of variation of each column for the given std & mean.
    """
    return (std / abs(mean)) * 100

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

def get_rng(data_max, data_min):
    """
    Computes the range of each column for the given max & min values.
    """
    return data_max - data_min

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

def get_fisher(dataset, mean, count, std):
    """
    Computes the Fisher's coefficient of each column for the given dataset.
    """
    fisher_list = np.array([])
    pos = 0
    for label in dataset:
        fisher_list = np.append(fisher_list, ((dataset[label] - mean[pos]) ** 3).sum())
        pos += 1
    return (fisher_list / count) / (std ** 3)

def get_kurtosis(dataset, mean, count, std):
    """
    Computes the Kurtosis' coefficient of each column for the given dataset.
    """
    kurtosis_list = np.array([])
    pos = 0
    for label in dataset:
        kurtosis_list = np.append(kurtosis_list, ((dataset[label] - mean[pos]) ** 4).sum())
        pos += 1
    return ((kurtosis_list / count) / (std ** 4)) - 3

if __name__ == '__main__':
    dataset = read_dataset()
    dataset = dataset.select_dtypes(include = 'number')
    data_count = get_count(dataset)
    data_mean = get_mean(dataset, data_count)
    data_var = get_var(dataset, data_count, data_mean)
    data_std = get_std(dataset, data_count, data_mean)
    data_cof = get_cof(data_std, data_mean)
    data_min = get_min(dataset)
    data_max = get_max(dataset)
    data_rng = get_rng(data_max, data_min)
    data_p25 = get_percentile(0.25, dataset, data_count)
    data_p50 = get_percentile(0.5, dataset, data_count)
    data_p75 = get_percentile(0.75, dataset, data_count)
    data_fisher = get_fisher(dataset, data_mean, data_count, data_std)
    data_kurtosis = get_kurtosis(dataset, data_mean, data_count, data_std)
    describe_values = [data_count, data_mean, data_var, data_std, data_cof, data_min, data_p25, data_p50, data_p75, data_max, data_rng, data_fisher, data_kurtosis]
    describe_index = ['count', 'mean', 'var', 'std', 'cof', 'min', '25%', '50%', '75%', 'max', 'rng', 'Fisher', 'Kurtosis']
    describe = pd.DataFrame(describe_values, index = describe_index, columns = dataset.columns)
    print("\n", describe, "\n")
    sys.exit(0)
