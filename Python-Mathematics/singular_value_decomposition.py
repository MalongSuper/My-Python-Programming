# Singular Value Decomposition
import numpy as np


# Function to choose AAT or ATA
def choose_space(A):
    m, n = A.shape

    if m >= n:
        print("\nUsing A^T A (Column Space)")
        M = A.T @ A
        mode = "ATA"
    else:
        print("\nUsing A A^T (Row Space)")
        M = A @ A.T
        mode = "AAT"

    return M, mode


# # Function to compute SVD
def compute_svd(A, M, mode):
    # Eigen decomposition
    eigenvalues, eigenvectors = np.linalg.eig(M)
    # Singular values
    sigma = np.sqrt(np.abs(eigenvalues))

    if mode == "ATA":
        # Right singular vectors
        V = eigenvectors
        # Compute U
        U = []
        for i in range(len(sigma)):
            if sigma[i] > 1e-10:
                ui = (A @ V[:, i]) / sigma[i]
                U.append(ui)
        U = np.array(U).T

    else:
        # Left singular vectors
        U = eigenvectors
        # Compute V
        V = []

        for i in range(len(sigma)):
            if sigma[i] > 1e-10:
                vi = (A.T @ U[:, i]) / sigma[i]
                V.append(vi)
        V = np.array(V).T

    return U, sigma, V


# User input
m, n = map(int, input("Enter matrix size (m, n): ").split(","))
# Random matrix
A = np.random.randint(1, 10, (m, n))
print("\nMatrix A:\n", A)
# Choose matrix space
M, mode = choose_space(A)
print("\nSelected Matrix:\n", M)
# Compute SVD
U, sigma, V = compute_svd(A, M, mode)
# Compact Sigma Matrix
Sigma = np.diag(sigma)

print("\nSingular Values:\n", sigma)
print("\nU Matrix:\n", U)
print("\nSigma Matrix:\n", Sigma)
print("\nV Matrix:\n", V)

# Reconstruct Matrix
A_reconstructed = U @ Sigma[:U.shape[1], :V.shape[0]] @ V.T
print("\nReconstructed Matrix:\n", np.round(A_reconstructed, 5))
