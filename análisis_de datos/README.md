# Data Analysis
The different statistical measures that have been used to describe the given dataset are: **count, mean, standard deviation, minimum value, maximum value, and percentiles.** Each of these measures gives us very valuable information about each column. We will be more prepared to study our dataset if we really understand what these values represent.<br>

All the mathematical formulas used to calculate these values have tried to be the same as those used by the **[Pandas library](https://pandas.pydata.org)**. In the case of quantiles, the result may vary by a few decimal places.

### [mean](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html)

<img align="right" width="500" alt="mean" src="https://user-images.githubusercontent.com/74931024/173940847-c0fefb99-6ee7-48d4-b1d9-fcf1544ab951.png">

Computes the mean value of each column for the given dataset. **The mean represents balance.** The mean is the value that each data would have if they were all the same. Since we are working with a sample and not with a population, what we calculate is the **sample mean** and not the mean itself.

### [std](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html)

<img align="right" width="500" alt="std" src="https://user-images.githubusercontent.com/74931024/173941053-93a90dd4-1c09-48a7-9405-e914940b2d62.png">

Computes the standard deviation value of each column for the given dataset. **The standard deviation measures the spread of the data for a given dataset.** The larger the standard deviation, the larger the population spread; the smaller the standard deviation, the smaller the population spread.<br><br>
As with the mean, what we calculate is the **sample standard deviation**, because we are working with a sample and not with a population. This is why we divide by **n - 1** and not just by **n**.

<img align="right" width="500" alt="percentile" src="https://user-images.githubusercontent.com/74931024/173941137-61091559-3f88-429d-92a2-c3556a00a01b.png">

### [percentile](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html)
Computes the specified percentile of each column for the given dataset.
