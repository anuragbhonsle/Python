
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


np.random.seed(42)
years = np.arange(2000, 2022)
sales = np.random.randint(500, 1000, size=len(years))


years = years.reshape(-1, 1)


X_train, X_test, y_train, y_test = train_test_split(years, sales, test_size=0.2, random_state=42)


model = LinearRegression()


model.fit(X_train, y_train)


future_years = np.arange(2022, 2030).reshape(-1, 1)
future_sales = model.predict(future_years)


plt.scatter(years, sales, label='Actual Sales')
plt.plot(years, model.predict(years), color='red', label='Linear Regression Model')
plt.scatter(future_years, future_sales, color='green', label='Predicted Sales (Future)')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Future Sales Predictor')
plt.legend()
plt.show()