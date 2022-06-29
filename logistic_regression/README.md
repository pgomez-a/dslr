# Logistic Regression

As we delve into the amazing world of **Machine Learning**, it's a good idea to cover as many algorithms as we can. Understanding different training algorithms will help us when we are in doubt about how to train our model. Therefore, I have implemented the option to select the algorithm that we want to use when training our model. In this way, we can compare the results obtained with the different algorithms used. The different training algorithms that have been implemented are:

- **Stochastic GD**
- **Mini-batch GD**
- **Batch GD**

### Gradient Descent

<img align = 'right' width="300" alt="gradient_descent" src="https://user-images.githubusercontent.com/74931024/175814121-fc6cbe88-fa80-448e-ba4a-729ae131aab4.png">

As we should know, one way to measure the reliability of our model is by calculating its error. In this way, **the smaller the error, the better our model will be**, since the predictions will be more adjusted to our training data. The fact that we can calculate the error of our model is due to the fact that we can represent it by means of a mathematical formula that represents this error. So, like any mathematical formula, it will have maximums, minimums, etc. Since we want to obtain the **minimum possible error**, what we are going to do is find the minimum point of the function (or one of them), and once there, we will know that it will have the best fitted model.<br>

**[I highly recommend that you read more about this algorithm.](https://www.analyticsvidhya.com/blog/2020/04/feature-scaling-machine-learning-normalization-standardization/)** There is a lot of information that is very important that I cannot cover in a few sentences. To complement the above information, I will say that we can find the minimum of the cost function by calculating its derivatives according to the weight parameters. For example, if our model depends on the constant weights **theta0** and **theta1**, we will calculate the derivatives of the cost function for **theta0** and **theta1**. In this way we will advance through the function in the attempt to achieve the minimum.
