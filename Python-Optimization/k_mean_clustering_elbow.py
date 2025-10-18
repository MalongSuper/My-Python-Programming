# K-Mean Clustering (Find the best K using Elbow Method)
# Calculate the sum of squared Euclidean distances
# between data points and their cluster center ("WCSS" or "inertia")
# Chooses the number of clusters where
# the change in the sum of squared distances starts to slow
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
        return compressed_data, centroids

    @staticmethod
    def calculate_inertia(data, centroids, labels):
        # Calculate the inertia (sum of squared distances from points to their centroids)
        inertia = 0
        for i in range(len(centroids)):
            cluster_points = data[labels == i]
            inertia += np.sum((cluster_points - centroids[i]) ** 2)
        return inertia

    @staticmethod
    def plot_inertia(inertia_values, min_k, max_k, optimal_k):
        #  Plot the inertia values for the Elbow Method
        plt.figure(figsize=(8, 6))
        plt.plot(range(min_k, max_k + 1), inertia_values, marker='o', linestyle='--', color='b')
        plt.title('Elbow Method For Optimal K')
        plt.xlabel('Number of Clusters (K)')
        plt.ylabel('Inertia (Sum of Squared Distances)')
        plt.xticks(range(min_k, max_k + 1))
        plt.grid(True)
        # Mark the optimal K with a vertical line and label
        plt.axvline(x=optimal_k, color='r', linestyle='-', label=f'Optimal K = {optimal_k}')
        plt.legend()
        # Show plot
        plt.show()

    def elbow_method(self, data):
        h, w = data.shape[0], data.shape[1]  # Get the image height and width
        # Constraints for min_K, max_K
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

        # Use the Elbow Method to find the optimal number of clusters (K).
        # The goal is to minimize inertia and look for an 'elbow' point.
        # Initialize variables to track inertia for different values of K
        inertia_values = []
        # Reshape the data into 2D Array of pixels (each row is a pixel with 3 color channels)
        data_reshaped = data.reshape(-1, 3)
        # Test for different values of K (from min_k to max_k)
        for k in range(min_k, max_k + 1):
            # Apply the K-Means Algorithm with K clusters (this gives us compressed image and centroids)
            compressed_data, centroids = self.apply_kmeans(data, k)
            # Get the labels of the data points (assigned to clusters)
            distances = dist.cdist(data_reshaped, centroids, metric='euclidean')
            labels = np.argmin(distances, axis=1)
            # Calculate inertia (sum of squared distances from data points to their centroids)
            inertia = self.calculate_inertia(data_reshaped, centroids, labels)
            inertia_values.append(inertia)
        # Find the "elbow" point where inertia starts to decrease slower
        # This is done by calculating the differences between consecutive inertia values
        inertia_diff = np.diff(inertia_values)
        inertia_diff2 = np.diff(inertia_diff)
        # The "elbow" is the point where the second derivative is closest to 0 (change of change)
        optimal_k = np.argmin(inertia_diff2) + 2  # +2 because of the double diff
        # Plot the inertia values to visualize the elbow
        self.plot_inertia(inertia_values, min_k, max_k, optimal_k)
        print(f"Optimal K found using the Elbow Method: {optimal_k}")
        return optimal_k


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
        optimal_k = kmeans.elbow_method(image_data)
        print(f"Optimal K: {optimal_k}")
        # Apply KMeans with the optimal K
        compressed_image, _ = kmeans.apply_kmeans(image_data, optimal_k)
        compressed_image = Image.fromarray(compressed_image)
        compressed_image.show()


main()
