# K-Mean Clustering, best K using Silhouette Method
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.spatial import distance as dist
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtCore import Qt
from PIL import Image


class KMean:
    def __init__(self, max_iters=100, tolerance=1e-4):
        self.max_iters = max_iters  # Maximum number of iterations
        self.tolerance = tolerance  # Threshold for the centroid movement

    def apply_kmeans(self, data, n_colors):
        labels = ''
        # Apply K-Mean Clustering with Scipy
        h, w, c = data.shape  # Get the image shape, typically (height, width, 3)
        data_reshaped = data.reshape(-1, 3)  # Reshape to 2D Array (use -1 instead of (h * w))
        # Step 1 - 2: Initialize centroids randomly from the data points
        # For example, if K = 16, we have 16 centroids
        centroids = np.array(random.sample(list(data_reshaped), n_colors))
        # Begin the K-Means iteration
        for iteration in range(self.max_iters):
            # Step 3: Assign each pixel to the nearest centroid using scipy cdist (faster than np.linalg.norm)
            # Step 3a: With K centroids, calculate the distance of the every centroid
            # to every point in the image, then choose the minimum one and mark its point
            distances = dist.cdist(data_reshaped, centroids, metric='euclidean')
            # Step 3b: With this, all the points are assigned to a cluster
            labels = np.argmin(distances, axis=1)
            # Step 4: Recalculate centroids as the mean of the assigned pixels
            # That is, we mark the center of each cluster
            # These center centroids are the new centroids of the cluster
            new_centroids = np.array([data_reshaped[labels == i].mean(axis=0) for i in range(n_colors)])
            # Handle empty clusters by reinitializing them to random data points
            for i in range(n_colors):
                if np.isnan(new_centroids[i]).any():
                    new_centroids[i] = data_reshaped[random.randint(0, data_reshaped.shape[0] - 1)]
            # Check for convergence
            if np.linalg.norm(new_centroids - centroids) < self.tolerance:
                break
            centroids = new_centroids
        # Step 5: Assign the final color (centroid) to each pixel
        compressed_data = centroids[labels].reshape(h, w, c).astype(int)
        return compressed_data, centroids, labels

    def silhouette_method(self, data):
        # Constraints for min_K, max_K
        h, w = data.shape[0], data.shape[1]  # Get the image height and width
        if h >= 8192 and w >= 8192:  # If the image is 8192x8192 or above
            # K is within [512, 1024]
            min_k, max_k = 512, 1024
        elif h >= 4096 and w >= 4096:  # If the image is 4096x4096 or above
            # K is within [256, 512]
            min_k, max_k = 256, 512
        elif h >= 2048 and w >= 2048:  # If the image is 2048x2048 or above
            # K is within [128, 256]
            min_k, max_k = 128, 256
        elif h >= 1024 and w >= 1024:  # If the image is 1024x1024 or above
            # K is within [64, 128]
            min_k, max_k = 64, 128
        elif h >= 512 and w >= 512:  # If the image is 512x512 or above
            # K is within [32, 64]
            min_k, max_k = 32, 64
        elif h >= 256 and w >= 256:  # If the image is 256x256 or above
            # K is within [16, 32]
            min_k, max_k = 16, 32
        else:  # If it is lower, K is fixed at 16
            min_k, max_k = 16, 16
        # Silhouette method
        data_reshaped = data.reshape(-1, 3)
        silhouette_scores = []
        for k in range(min_k, max_k + 1):  # Loop through different K
            _, _, labels = self.apply_kmeans(data, k)
            n_samples = data_reshaped.shape[0]  # Height of the image
            silhouette_score = []
            # Formula s[i] = (b[i] - a[i]) / max(a[i], b[i])
            # a[i]: Mean distance from a data point to all other points in the same cluster
            # b[i]: Mean distance from a data point to all points in the nearest cluster
            # (the point does not belong to the cluster itself)
            for i in range(n_samples):
                # Step 1: Calculate a[i]
                point_cluster = data_reshaped[labels == labels[i]]  # Get the point belong to the cluster
                ai = np.mean(np.linalg.norm(point_cluster - data_reshaped[i], axis=1))
                # Step 2: Calculate b[i]
                not_clusters = np.unique(labels[labels != labels[i]])  # Get the unique cluster
                bi = float('inf')  # Initialize b(i) to infinity
                for cluster in not_clusters:
                    point_not_cluster = data_reshaped[labels == cluster]  # Get the point not belong to the cluster
                    bi = min(bi, np.mean(np.linalg.norm(point_not_cluster - data_reshaped[i])))
                # Step 3: Find the silhouette score s[i]
                si = (bi - ai) / max(ai, bi)
                silhouette_score.append(si)
            # Get the average silhouette score across all samples
            mean_silhouette_score = np.mean(silhouette_score)
            silhouette_scores.append(mean_silhouette_score)
            print(f"Silhouette Score for K={k}: {mean_silhouette_score}")
            # Draw a plot (for reference
            self.plot_silhouette_score(silhouette_scores, min_k, max_k)
            # Return the best K with the highest silhouette score
            best_k = np.argmax(silhouette_scores) + 2  # Adding 2 because we started from K=2
            print(f"Best K: {best_k} with Silhouette Score: {silhouette_scores[best_k - 2]}")
            return best_k

    @staticmethod
    def plot_silhouette_score(silhouette_scores, min_k, max_k):
        # Plot the silhouette scores for each K
        plt.figure(figsize=(8, 6))
        plt.plot(range(min_k, max_k + 1), silhouette_scores, marker='o')
        plt.title('Silhouette Score for Different Values of K')
        plt.xlabel('Number of Clusters (K)')
        plt.ylabel('Silhouette Score')
        plt.show()


def load_image():
    # Initialize Qt application
    app = QApplication([])
    print(app)
    # Open file dialog to select an image
    file_path, _ = QFileDialog.getOpenFileName(None, "Select an Image",
                                               "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
    if file_path:
        image = Image.open(file_path)
        image_data = np.array(image)
        print(f"Size: {image_data.shape[0]} x {image_data.shape[1]}")
        print(f"Pixels: {image_data.shape[0] * image_data.shape[1]}")
        return image_data
    else:
        print("No file selected")
        return None


def main():
    image_data = load_image()
    kmeans = KMean()
    if image_data is not None:
        # Find the optimal K using Elbow Method
        optimal_k = kmeans.silhouette_method(image_data)
        print(f"Optimal K: {optimal_k}")
        # Apply KMeans with the optimal K
        compressed_image, _, _ = kmeans.apply_kmeans(image_data, optimal_k)
        compressed_image = Image.fromarray(compressed_image)
        compressed_image.show()


main()
