# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ktj8TruEI8tCKId8BWfM1TH60xqPHtjC

**Simple linear regression**

importing libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""importing dataset"""

dataset = pd.read_csv('/content/sample_data/Salary_Data (3) (1) - Salary_Data (3) (1).csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

"""splitting dataset into traing set and test set"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3,random_state=0)

"""training the simple linear regression model on the training set


"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

"""Prediction on the test set results"""

y_pred = regressor.predict(x_test)

"""Visualizing"""

plt.scatter(x_train, y_train, color = 'blue')
plt.plot(x_train, regressor.predict(x_train), color = 'red')
plt.title("Salary vs Experience  (trainng set)")
plt.xlabel("Experience")
plt.ylabel("Salary")