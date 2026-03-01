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
data = data.select_dtypes(include=["number"]).dropna()

# Features for clustering (ignore target)
X_train = data.iloc[:, :-1].to_numpy()

# -----------------------------------------
# Different k values
# -----------------------------------------
k_values = [2, 3, 4, 5, 7, 9, 11, 8, 6, 7]
ans = []

for i in k_values:
    kmeans = KMeans(
        n_clusters=i,
        random_state=0,
        n_init="auto"
    ).fit(X_train)

    # Using inertia (better than len(cluster_centers))
    ans.append(kmeans.inertia_)

# -----------------------------------------
# Plot
# -----------------------------------------
plt.plot(k_values, ans, marker='o')
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.title("K-Means Evaluation using Inertia")
plt.show()