# Data Analysis
The different statistical measures that have been used to describe the given dataset are: **count, mean, standard deviation, minimum value, maximum value, and percentiles.** Each of these measures gives us very valuable information about each column. We will be more prepared to study our dataset if we really understand what these values represent.<br>

All the mathematical formulas used to calculate these values have tried to be the same as those used by the **[Pandas library](https://pandas.pydata.org)**. In the case of quantiles, the result may vary by a few decimal places.

## Centralization Measures
They only make sense if they are used with numeric values. **They are values around which the data is grouped.**

### [mode](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html)
The **mode** is the **value with the highest absolute frequency**, that is, it's the value that is repeated the most. An important aspect to keep in mind is that there may or may not be a mode (if all values have the same absolute frequency). Furthermore, if for example there are two different values with the highest absolute frequency, we say that the data distribution is **bimodal.**

### [mean](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html)

<img align="right" width="500" alt="mean" src="https://user-images.githubusercontent.com/74931024/174411012-1ec56e4a-c9d9-4d94-934c-7ee6fd641066.png">

**The mean represents balance.** The mean is the value that each data would have if they were all the same. Since we are working with a sample and not with a population, what we calculate is the **sample mean** and not the mean itself.

- **Contains more information** than the median because it uses the values of all the data.
- It's easier to calculate than the median.

### [median](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html)
The **median** is a value that, ordered from smallest to largest, 50% of the data is less than or equal to this value and the other 50% is greater than or equal to it. With ordered data, if there are an odd number of values, the median is the value in the middle. If there is an even number of values, the median is the half sum of the two middle values. The median corresponds to the 50th percentile.

- **It's more robust to changes** in the data than the mean.

## Dispersion Measures
They complete the information provided by the centralization measures and **indicate whether they are more or less representative of the dataset.** As the measure gets smaller, the spread of the data in the dataset decreases.

<img align="right" width="500" alt="range" src="https://user-images.githubusercontent.com/74931024/174412212-179002c6-766d-45b9-b86b-79e8c5b5c139.png">
<br>

### range
The range measures the amplitude of data.

### [variance](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html)

<img align="right" width="500" alt="variance" src="https://user-images.githubusercontent.com/74931024/174411273-004855db-70bf-4549-8c84-88605361dccb.png">

**The variance represents a type of mean distance of the data from the sample mean.** The greater the variance, the greater the distance between the data and the sample mean and the less representativeness of the sample mean in that dataset. The variance is always greater than or equal to 0, because it's measured in units squared. As with the mean, what we calculate is the **sample variance**, because we are working with a sample and not with a population. This is why we divide by **n - 1** and not just by **n**.

### [standard deviation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html)

<img align="right" width="500" alt="standard deviation" src="https://user-images.githubusercontent.com/74931024/174411349-4d6e92fd-bf04-49b2-a7c1-d1dfada60097.png">

**The standard deviation measures the spread of the data for a given dataset.** The larger the standard deviation, the larger the population spread; the smaller the standard deviation, the smaller the population spread. In fact, what we really do is the square root of the variance so that we can work with simple units and not with units squared.

### coefficient of variation

<img align="right" width="500" alt="coefficient of variation" src="https://user-images.githubusercontent.com/74931024/174411453-438d5a40-3911-490a-8c42-a956cbe6675c.png">

Variance cannot be used as a measure of dispersion if what we want is to **compare, among different datasets,** which is the most dispersed with respect to the sample mean, unless all the datasets have the same sample mean. To achieve this, without having to worry about the sample mean, we work with the **coefficients of variation**, which **eliminate the influence of the sample mean and the magnitude and units of the data.** If we multiply the result by 100, we get a percentage.

### [percentile](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html)

<img align="right" width="500" alt="percentile" src="https://user-images.githubusercontent.com/74931024/174411622-46f60da4-17d8-42e5-a710-fb47791aac77.png">

**A percentile is a positional statistical measure that divides the ordered distribution of data into one hundred equal parts.** This measure shows the observations for a variable that are below a specified percentage.

## Shape Measures

### Fisher's coefficient
It gives us an idea of the **symmetry or asymmetry** of the data distribution **(hene its shape)** and allows us to compare different datasets.
- **CAF > 0** - The distribution is asymmetric to the right.
- **CAF = 0** - The distribution is symmetric.
- **CAF < 0** - The distribution is asymmetric to the left.

### Kurtosis coefficient
With this coefficient we get an idea of how **“spiky”** or **“flat”** a distribution is **(hence its shape)** compared to a standard distribution: the normal distribution.
- **Kurtosis > 0** - The data distribution is more "spiky" than the normal distribution with the same mean and variance as the data.
- **Kurtosis = 0** - The data distribution is just as “spiky” as the normal distribution with the same mean and variance as the data.
- **Kurtosis < 0** - The data distribution is less "spiky" than the normal distribution with the same mean and variance as the data.
