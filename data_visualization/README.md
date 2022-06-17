# Data Visualization
**Data visualization** is a very complex field that can be extended as much as desired. Since the goal of this project is to introduce you to different Machine Learning concepts, we will only have to cover a few data visualization tasks. To achieve this, our goal will be to find graphs that allow us to find an answer to these three questions:

- **Which Hogwarts course has a homogeneous score distribution between all four houses?**
- **What are the two features that are similar?**
- **What features are you going to use for your logistic regression?**

To answer each question, we are going to use different graphs, which will be explained below.

### [Histogram](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)
A **histogram** is a graphical representation in the form of bars that shows the distribution of a dataset. They are used to get a first idea of the **distribution of a population or a sample** with respect to a continuous or qualitative characteristic. The x-axis corresponds to the range of values to which the data belong; while the y-axis represents the frequency of each range. This frequency can be:

- **Absolute frequency.**
- **Relative frequency.**

<div align="center">
<img width="500" alt="absolute" src="https://user-images.githubusercontent.com/74931024/174194644-6f45a72f-084c-47e5-8103-258e3bd03f22.png">
<img width="500" alt="relative" src="https://user-images.githubusercontent.com/74931024/174194659-d023fb69-8237-41c4-8b72-3c41dbc3e9bf.png">
</div>

### [Scatter Plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html)
**Scatter plots** are graphs used to plot data on a horizontal and vertical axis to show how much one variable influences another. **The relationship between two variables is called correlation.** If the indicators show an almost straight line on the scatterplot, the correlation is high. If the indicators are evenly distributed across the entire scatterplot, the correlation is low or even null. In addition, we must take into account that we could study an apparent correlation between variables when the truth is that these variables could be influenced by another variable. So we also have to be aware of the limitations of this measure.

<div align="center">
<img width="500" alt="scatter 1" src="https://user-images.githubusercontent.com/74931024/174317882-171e240e-b221-4997-a30a-99f1afccb16a.png">
<img width="500" alt="scatter 2" src="https://user-images.githubusercontent.com/74931024/174317988-13c9ccac-447e-48f5-adde-243ddecbc781.png">
</div>
