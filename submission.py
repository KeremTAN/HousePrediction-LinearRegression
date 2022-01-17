import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

# data loaded
data = pd.read_csv('data/prices.csv')

# necessary object
linearReg = LinearRegression()

# pre-processing of data
prices = pd.DataFrame(data=data["price"], index=range(len(data)))

features = pd.DataFrame(data=data.iloc[:, 1:], index=range(len(data)))

x_train, x_test, y_train, y_test = train_test_split(features, prices, test_size=0.2, random_state=0)

linearReg.fit(x_train, y_train)
y_predictions = linearReg.predict(x_test)

print(f"-- Our Predictions --\n {y_predictions}")
print(f"R2 score is {r2_score(y_test, y_predictions)}")
print(f"Root Mean Squared Error(RMSE) is {np.sqrt(mean_squared_error(y_test, y_predictions))}")
