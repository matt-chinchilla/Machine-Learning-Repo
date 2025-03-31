# Training and running a linear model using Scikit-Learn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Download and prepare the data
data_root = "https://github.com/ageron/data/blob/main/lifesat/"
lifesat = pd.read_csv(data_root + "lifesat.csv") # Life satisfaction data
x = lifesat[["GDP per capita (USD)"]].values
y = lifesat["Life satisfaction"].values

# Visualize the data
lifesat.plot(kind='scatter', grid=True,
             x="GDP per capita (USD)", y="Life satisfaction")
plt.axis([23_500, 32_500, 4, 9])
plt.show()

# Select a linear model
model = LinearRegression()

# train the model
model.fit(x, y)

# Make a predicton for Cyrpus
X_new = [[37_655.2]]    # Cyprus' GDP per capita in 2020
print(model.predict(X_new))