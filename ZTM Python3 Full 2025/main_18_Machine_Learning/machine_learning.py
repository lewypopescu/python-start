# Steps for knowledge: Machine Learning
# 1 - Import the data
# 2 - Clean the data
# 3 - Split the data. Training Set, Test Set: 80/20, means 80% training, 20% testing
# 4 - Create a model
# 5 - Check the output/Train the model
# 6 - Improve/Make predictions

# Think of Machine Learning as an iterative process:
# You input data => the algorithm finds patterns => the model learns => you test it => you improve it.
# The goal is for the model to make accurate predictions on new data it has never seen before.

# Numpy is the main library for working with arrays in Python
# Pandas is the main library for working with dataframes in Python
# Scikit-learn is the main library for working with machine learning in Python: it merges many algorithms and tools for machine learning
# Matplotlib is the main library for working with data visualization in Python

# Jupyter Notebook is an interactive environment for running Python code, visualizing data, and documenting the process, commonly used in data science and machine learning projects.

# Simple Linear Regression Example
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Create a simple dataset
# Suppose we have data about houses: size (m²) and price (thousand €)
data = {
    'size': [50, 60, 80, 100, 120, 150],
    'price': [150, 180, 220, 260, 300, 360]
}

df = pd.DataFrame(data)

# Split the data (80% training, 20% testing)
X = df[['size']]   # feature(s)
y = df['price']    # target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Visualize the results
plt.scatter(X, y, color='blue', label='Real data')
plt.plot(X, model.predict(X), color='red', label='Model prediction')
plt.xlabel('House size (m²)')
plt.ylabel('Price (thousand €)')
plt.legend()
plt.show()

# Predict a new house
new_house = np.array([[130]])
predicted_price = model.predict(new_house)
print(
    f"Predicted price for a 130 m² house: {predicted_price[0]:.2f} thousand €")
