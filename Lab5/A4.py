import pandas as pd
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
# Keep only numeric columns
data = data.select_dtypes(include=["number"]).dropna()

# -----------------------------------------
# Features for clustering (ignore target)
# -----------------------------------------
X_train = data.iloc[:, :-1].to_numpy()

# -----------------------------------------
# K-Means clustering (k = 2)
# -----------------------------------------
kmeans = KMeans(
    n_clusters=2,
    random_state=0,
    n_init="auto"
).fit(X_train)

# -----------------------------------------
# Output
# -----------------------------------------
labels = kmeans.labels_
centers = kmeans.cluster_centers_

print("Cluster Labels:")
print(labels)

print("\nCluster Centers:")
print(centers)