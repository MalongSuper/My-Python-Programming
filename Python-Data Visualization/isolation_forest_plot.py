# Isolation Forest to detect outliers
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def plot_outliers(x, y, i, title):
    # Draw scatter plot (petal length + width)
    axes[i].scatter(normal[x], normal[y], label="Normal", alpha=0.7)
    axes[i].scatter(outliers[x], outliers[y], label="Outliers", color="red", s=60)

    axes[i].set_title(title)
    axes[i].legend()


def plot_pca(pc1, pc2):
    plt.figure(figsize=(8, 6))

    plt.scatter(normal[pc1], normal[pc2],
                alpha=0.7, label="Normal")
    plt.scatter(outliers[pc1], outliers[pc2],
                color='red', s=60, label="Outliers")

    plt.title("PCA Projection of Iris Dataset with Outliers")
    plt.xlabel(pc1)
    plt.ylabel(pc2)
    plt.legend()
    plt.grid(True)

    plt.show()


# Load the iris dataset
df = pd.read_csv('dav_datasets/iris_with_outliers.csv')
# Isolation Forest to detect outliers
model = IsolationForest(contamination=0.1)
model.fit(df.drop('target', axis=1))

# The predict method returns labels indicating
# whether each data point is classified as normal (1) or anomalous (-1) by the model.
df['outlier'] = model.predict(df.drop('target', axis=1))

# Display the results (outliers only)
normal = df[df['outlier'] == 1]
outliers = df[df['outlier'] == -1]
print(outliers.head(10))

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

plot_outliers(x="sepal length (cm)", y="sepal width (cm)", i=0,
              title="Sepal Length and Width")
plot_outliers(x="petal length (cm)", y="petal width (cm)", i=1,
              title="Petal Length and Width")

plt.tight_layout()
plt.show()

print("Method 2: PCA")
pca = PCA(n_components=2)
df_temp = df.drop(['target', 'outlier'], axis=1)
df_pca = pca.fit_transform(df_temp)
df['PC1'] = df_pca[:, 0]
df['PC2'] = df_pca[:, 1]
normal = df[df['outlier'] == 1]
outliers = df[df['outlier'] == -1]
plot_pca(pc1='PC1', pc2='PC2')