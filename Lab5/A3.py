import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error, r2_score

# -----------------------------------------
# Load dataset
# -----------------------------------------
data = pd.read_excel(
    r"C:\Users\jagan\OneDrive\Documents\sem4\ml\LAB4\ml_dataset.csv"
)

# -----------------------------------------
# Preprocessing
# -----------------------------------------
data = data.select_dtypes(include=["number"]).dropna()

# -----------------------------------------
# Multiple features (like ['we','were','what','when'])
# Here: first 4 numeric columns
# -----------------------------------------
X_train = data[data.columns[:4]].to_numpy()

# Target: last column
y_train = data[data.columns[-1]].to_numpy()

# -----------------------------------------
# Train Linear Regression
# -----------------------------------------
reg = LinearRegression().fit(X_train, y_train)

# Predictions
y_predicted = reg.predict(X_train)

# -----------------------------------------
# Metrics function (your style)
# -----------------------------------------
def get_metrics(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mape = mean_absolute_percentage_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return [mse, rmse, mape, r2]

# -----------------------------------------
# Print results
# -----------------------------------------
results = get_metrics(y_train, y_predicted)
METRICS = ['mse', 'rmse', 'mape', 'r2']

print("\nMODEL PERFORMANCE METRICS")
for name, value in zip(METRICS, results):
    print(f"{name} : {value}")