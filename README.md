# dslr

<img width="1098" alt="dslr" src="https://user-images.githubusercontent.com/74931024/175793932-d9d802f6-29a4-4b70-b171-a2dab268c815.png">

**If you want to learn more about IT topics, [I invite you to join my Patreon channel](https://www.patreon.com/pgomeza) and visit my website:** [**IA Notes**](https://ia-notes.com/)

*On no! Since its creation, the famous school of wizards, Hogwarts, had never known such an offense. The forces of evil have bewitched the Sorting Hat. It no longer responds, and is unable to fulfill his role of sorting the students to the houses.<br>
The new academic year is approaching. Gladly, the Professor McGonagall was able to take action in such a stressful situation, since it is impossible for Hogwarts not to welcome new students... She decided to call on you, a muggle "datascientist" who is able to create miracles with the tool which all muggles know how to use: a "computer".<br>
Despite the intrinsic reluctance of many wizards, the director of the school welcomes you to his office to explain the situation. You are here because his informant discovered that you are able to recreate a magic Sorting Hat using your muggle tools. You explain to him that in order for your "muggle" tools to work, you need students data. Hesi- tantly, Professor McGonagall gives you a dusty spellbook. Fortunately for you, a simple "Digitalis!" and the book turned into a USB stick.<br>*

In this project **DataScience x Logistic Regression,** we will continue our exploration of Machine Learning by discovering different tools. We will implement a linear classification model, as a continuation of the subject linear regression : **a logistic regression.**

### Data Analysis
According to **[Wikipedia](https://en.wikipedia.org/wiki/Data_analysis)**: *"**Data analysis is a process of inspecting, cleaning, transforming, and modelling data with the goal of discovering useful information, informing conclusions, and supporting decision-making.**"*<br>

Before we start training our model, **we need to study the available data.** This way we can get an idea of the results we hope to achieve and the things we can achieve. This first step is very important in the field of Machine Learning, because if we want to understand what we are doing, we must first understand what we have. Once we understand the tools we have and the data available, we will be much more prepared to implement a Machine Learning model capable of adapting to the data.<br>

For this reason, the first thing we need to do in **dslr** is to create an executable that describes the contents of a given database. This program will obtain the numerical columns of said database and will show different statistical measures related to each column, such as: **count, mean, standard deviation, percentiles, etc.** Thanks to this, we will be able to get an idea of the main objective that we want to achieve, which is to be able to classify each Hogwarts student in their respective houses.<br>

For more information on the mathematical formulas used to calculate the statistical measures, **[click here.](https://github.com/pgomez-a/dslr/tree/main/data_analysis)**

<img align="center" width="850" alt="describe" src="https://user-images.githubusercontent.com/74931024/175771479-19242b23-9558-4170-82ca-8eab7d6c2240.png">

### Data Visualization
According to **[Wikipedia](https://en.wikipedia.org/wiki/Data_and_information_visualization)**: *"**data visualization is an interdisciplinary field that deals with the graphic representation of data and information.**"*

Another important step that we must take before training our model is to visualize the available data. We have calculated and studied different statistical measures that have provided us with very useful information about the problem we want to solve. But we can get more information just as valuable simply by visualizing the data. Thanks to this we will be able to understand, among other things, **how the data is distributed, the dependency that exists between the variables, etc.**<br>

The second part of **dslr** is to create different executables that show us different graphs related to the data. In this way, we will be more prepared for the third step, when we study the best training algorithm to fit our data. We will be able to make a better decision about this algorithm if we consider the information we have obtained from data analysis and data visualization.<br>

For more information on the statistical graphs used to study the available data, **[click here.](https://github.com/pgomez-a/dslr/tree/main/data_visualization)**

<div align="center">
<img width="410" alt="histogram" src="https://user-images.githubusercontent.com/74931024/174310059-afee3390-35db-4015-bf0c-2535967da865.png">
<img width="410" alt="scatter plot" src="https://user-images.githubusercontent.com/74931024/174310127-6d693c4a-5cc6-4d85-a851-860e4736f235.png">
<img width="900" alt="pair plot" src="https://user-images.githubusercontent.com/74931024/174330795-8aa7e669-f0c4-4fcb-8c2b-897726527baf.png">
</div>

### Logistic Regression
According to **[Wikipedia](https://en.wikipedia.org/wiki/Logistic_regression)**: *"**logistic model is a statistical model that models the probability of one event taking place by having the log-odds for the event be a linear combination of one or more independent variable.**"*

The third part of **DSLR** is to train a **logistic regression** model with the provided datasets. However, instead of explaining in a few sentences what this model is about, I encourage you to complete the **[Machine Learning bootcamp](https://github.com/pgomez-a/42_ML_Piscine)** developed by the **[42-AI team](https://www.42ai.fr)**. I think that if you try to do all the tasks that have been given to you, you will get a deep understanding of how this model works. At the end of the day, there is a lot of math and statistics involved in these types of projects, so spending a little more time early on will go a long way for us in the future.<br>

Similarly, if you prefer to start with a simpler project, I advise you to do the **[ft_linear_regression project](https://github.com/pgomez-a/ft_linear_regression)**. This project will introduce you to the world of **Machine Learning** by training a simple linear regression model. Most of the concepts we use in this logistic regression project are taken from linear regression, so this could be a good starting point if you want to delve into this amazing world of data understanding.<br>

For more information on the training algorithms used to calculate the tightest weights, **[click here.](https://github.com/pgomez-a/dslr/tree/main/logistic_regression)**

<img width="900" alt="train" src="https://user-images.githubusercontent.com/74931024/176227435-e273a67b-e651-4a23-8e37-cc4972b785b6.png">
