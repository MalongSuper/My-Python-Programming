# K-Mean Clustering Visualization for Image Compression Problem
# Reference to this video to understand K-Mean Clustering
# https://www.youtube.com/watch?v=GZj6ikx8PAc
import numpy as np  # For array or matrix calculations
import matplotlib.pyplot as plt  # For plot
import cv2  # For image and video procession
from sklearn.cluster import KMeans  # For KMeans algorithm
from sklearn.decomposition import PCA  # For 2D plot using PCA

# Step 1: Get user input for image size and number of clusters
try:
    image_height = int(input("Enter image height (e.g., 256): "))
    image_width = int(input("Enter image width (e.g., 256): "))
    K = int(input("Enter number of clusters (K) (e.g., 16): "))
except ValueError:
    print("Invalid input. Please enter integers only.")
    exit()

# Step 2: Generate a random image with the given dimensions
# Each pixel will have 3 color channels (R, G, B) with values from 0 to 255
np.random.seed(42)  # For reproducibility
original_image = np.random.randint(0, 256, (image_height, image_width, 3), dtype=np.uint8)
# Step 3: Reshape image to (num_pixels, 3) - Each row is a pixel with 3 RGB values
pixels = original_image.reshape((-1, 3))  # Shape: (image_height * image_width, 3)
# Step 4: Apply K-Means Clustering - Reduce colors from 16.7M to K
print("Applying K-Means clustering. This may take a moment...")
kmeans = KMeans(n_clusters=K, random_state=42)
kmeans.fit(pixels)

# Get the cluster centers (dominant colors) and labels for each pixel
cluster_centers = np.uint8(kmeans.cluster_centers_)
labels = kmeans.labels_  # Shape: (image_height * image_width,)
# Step 5: Recolor the image using the K dominant colors
compressed_pixels = cluster_centers[labels]  # Replace each pixel with its cluster's color
compressed_image = compressed_pixels.reshape((image_height, image_width, 3))  # Shape: (image_height, image_width, 3)

# Step 6: Plot the original and compressed images side by side
fig, axes = plt.subplots(1, 2, figsize=(9, 6))
axes[0].imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
axes[0].set_title(f'Original Image ({image_height}x{image_width})')
axes[0].axis('off')
axes[0].text(0.5, -0.1, f'Pixels: {image_height * image_width}',
             ha='center', va='top', transform=axes[0].transAxes, fontsize=12)

axes[1].imshow(cv2.cvtColor(compressed_image, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for display
axes[1].set_title(f'Compressed Image (K={K} Colors)')
axes[1].axis('off')
axes[1].text(0.5, -0.1, f'Pixels: {image_height * image_width}',
             ha='center', va='top', transform=axes[1].transAxes, fontsize=12)

plt.tight_layout()
plt.show()

# Step 7: Plot clusters in 3D RGB space to see color grouping
# Select a random sample of 1000 points for better visualization
print("Plotting 3D RGB space for color clustering...")
sampled_pixels = pixels[np.random.choice(pixels.shape[0], min(1000, pixels.shape[0]), replace=False)]
sampled_labels = kmeans.predict(sampled_pixels)

# Plot the clusters in 3D RGB space
plot = plt.figure(figsize=(9, 6))
ax = plot.add_subplot(111, projection='3d')

# Each color in the plot represents a cluster, showing how pixels are grouped
for i in range(K):
    cluster_points = sampled_pixels[sampled_labels == i]  # Points in this cluster
    ax.scatter(cluster_points[:, 0], cluster_points[:, 1], cluster_points[:, 2], s=5)

ax.set_xlabel('Red Channel')
ax.set_ylabel('Green Channel')
ax.set_zlabel('Blue Channel')
ax.set_title('RGB Color Space Clustering (Sampled Pixels)')
plt.show()

# Step 8: Plot clusters in 2D space using PCA
print("Reducing 3D RGB space to 2D using PCA...")
pca = PCA(n_components=2)
pca_pixels = pca.fit_transform(pixels)  # Shape: (image_height * image_width, 2)
sampled_pca_pixels = pca_pixels[np.random.choice(pca_pixels.shape[0],
                                                 min(1000, pca_pixels.shape[0]), replace=False)]
sampled_pca_labels = kmeans.predict(pixels[np.random.choice(pixels.shape[0],
                                                            min(1000, pixels.shape[0]), replace=False)])

# Plot the clusters in 2D PCA space
plt.figure(figsize=(9, 6))
for i in range(K):
    cluster_points = sampled_pca_pixels[sampled_pca_labels == i]  # Points in this cluster
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], s=8)

plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('2D PCA Projection of RGB Clusters')
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
plt.show()
