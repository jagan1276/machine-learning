import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# -----------------------------------------
# Load dataset
# -----------------------------------------
data = pd.read_excel(
    r"C:\Users\jagan\OneDrive\Documents\sem4\ml\LAB4\ml_dataset.csv"
)

# -----------------------------------------
# Preprocessing
# -----------------------------------------
# Keep only numeric columns and remove NaN
data = data.select_dtypes(include=["number"]).dropna()

# -----------------------------------------
# Features for clustering (ignore target)
# -----------------------------------------
X_train = data.iloc[:, :-1].to_numpy()

# -----------------------------------------
# Elbow Method
# -----------------------------------------
distortions = []
k = list(range(2, 20))

for i in k:
    kmeans = KMeans(
        n_clusters=i,
        random_state=42,
        n_init="auto"
    ).fit(X_train)
    distortions.append(kmeans.inertia_)

# -----------------------------------------
# Plot
# -----------------------------------------
plt.plot(k, distortions, marker='o')
plt.xlabel("Number of clusters (k)")
plt.ylabel("Distortion (Inertia)")
plt.title("Elbow Method for Optimal k")
plt.show()