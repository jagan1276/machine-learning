import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score

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
# K-Means clustering (k = 2)
# -----------------------------------------
kmeans = KMeans(n_clusters=2, random_state=42, n_init="auto")
kmeans.fit(X_train)

# -----------------------------------------
# Clustering evaluation metrics
# -----------------------------------------
sil = silhouette_score(X_train, kmeans.labels_)
ch = calinski_harabasz_score(X_train, kmeans.labels_)
db = davies_bouldin_score(X_train, kmeans.labels_)

# -----------------------------------------
# Output
# -----------------------------------------
print("Silhouette Score        :", sil)
print("Calinski-Harabasz Score :", ch)
print("Davies-Bouldin Index    :", db)