# Data Analysis
The different statistical measures that have been used to describe the given dataset are: **count, mean, standard deviation, minimum value, maximum value, and percentiles.** Each of these measures gives us very valuable information about each column. We will be more prepared to study our dataset if we really understand what these values represent.<br>

All the mathematical formulas used to calculate these values have tried to be the same as those used by the **[Pandas library](https://pandas.pydata.org)**. In the case of quantiles, the result may vary by a few decimal places.

## Centralization Measures
They only make sense if they are used with numeric values. **They are values around which the data is grouped.**

### [mode](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html)
The **mode** is the **value with the highest absolute frequency**, that is, it's the value that is repeated the most. An important aspect to keep in mind is that there may or may not be a mode (if all values have the same absolute frequency). Furthermore, if for example there are two different values with the highest absolute frequency, we say that the data distribution is **bimodal.**

### [mean](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html)

<img align="right" width="500" alt="mean" src="https://user-images.githubusercontent.com/74931024/173940847-c0fefb99-6ee7-48d4-b1d9-fcf1544ab951.png">

Computes the mean value of each column for the given dataset. **The mean represents balance.** The mean is the value that each data would have if they were all the same. Since we are working with a sample and not with a population, what we calculate is the **sample mean** and not the mean itself.

- **Contains more information** than the median because it uses the values of all the data.
- It's easier to calculate than the median.

### [median](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html)
The **median** is a value that, ordered from smallest to largest, 50% of the data is less than or equal to this value and the other 50% is greater than or equal to it. With ordered data, if there are an odd number of values, the median is the value in the middle. If there is an even number of values, the median is the half sum of the two middle values. The median corresponds to the 50th percentile.

- **It's more robust to changes** in the data than the mean.

## Dispersion Measures
They complete the information provided by the centralization measures and **indicate whether they are more or less representative of the dataset.** As the measure gets smaller, the spread of the data in the dataset decreases.

### [std](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html)

<img align="right" width="500" alt="std" src="https://user-images.githubusercontent.com/74931024/173956465-4fb26ca5-aa5b-44ea-aaf4-e759e880652f.png">

Computes the standard deviation value of each column for the given dataset. **The standard deviation measures the spread of the data for a given dataset.** The larger the standard deviation, the larger the population spread; the smaller the standard deviation, the smaller the population spread.<br><br>
As with the mean, what we calculate is the **sample standard deviation**, because we are working with a sample and not with a population. This is why we divide by **n - 1** and not just by **n**.

### [percentile](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html)

<img align="right" width="500" alt="percentile" src="https://user-images.githubusercontent.com/74931024/173941137-61091559-3f88-429d-92a2-c3556a00a01b.png">

Computes the specified percentile of each column for the given dataset. **A percentile is a positional statistical measure that divides the ordered distribution of data into one hundred equal parts.** This measure shows the observations for a variable that are below a specified percentage.
