import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
data = pd.read_excel(
    r"C:\Users\jagan\OneDrive\Documents\sem4\ml\LAB4\ml_dataset.csv"
)

# Keep only numeric data and remove missing values
data = data.select_dtypes(include=["number"]).dropna()

# Feature (single column)
X_train = data[[data.columns[0]]].to_numpy()

# Target (last column)
y_train = data[data.columns[-1]].to_numpy()

# Train Linear Regression model
reg = LinearRegression().fit(X_train, y_train)

# Prediction
y_predicted = reg.predict(X_train)

print("Predicted values:")
print(y_predicted)