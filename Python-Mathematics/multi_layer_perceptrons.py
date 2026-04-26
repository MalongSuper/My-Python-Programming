import numpy as np
import pandas as pd


# Activation + Loss
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def binary_cross_entropy(y, y_hat):
    eps = 1e-9
    return -np.mean(y * np.log(y_hat + eps) +
                    (1 - y) * np.log(1 - y_hat + eps))


# Adam Optimizer
def adam_update(W, b, dW, db, m_w, v_w, m_b, v_b, t,
                lr=0.01, beta1=0.9, beta2=0.999, eps=1e-8):

    # First moment
    m_w = beta1 * m_w + (1 - beta1) * dW
    m_b = beta1 * m_b + (1 - beta1) * db

    # Second moment
    v_w = beta2 * v_w + (1 - beta2) * (dW ** 2)
    v_b = beta2 * v_b + (1 - beta2) * (db ** 2)

    # Bias correction
    m_w_hat = m_w / (1 - beta1 ** t)
    v_w_hat = v_w / (1 - beta2 ** t)

    m_b_hat = m_b / (1 - beta1 ** t)
    v_b_hat = v_b / (1 - beta2 ** t)

    # Update
    W -= lr * m_w_hat / (np.sqrt(v_w_hat) + eps)
    b -= lr * m_b_hat / (np.sqrt(v_b_hat) + eps)

    return W, b, m_w, v_w, m_b, v_b


# Dataset
data = {
    "prio": [120,110,115,100,125,105,118,102,122,108],
    "static_prio": [120,110,115,100,120,105,118,102,120,108],
    "normal_prio": [120,110,115,100,125,105,118,102,122,108],
    "policy": [0,1,0,1,0,1,0,1,0,1],
    "vm_pgoff": [1024,4096,2048,8192,512,6000,1500,7000,900,5000],
    "class": [0,1,0,1,0,1,0,1,0,1]
}

df = pd.DataFrame(data)

X = df.drop(columns="class").values
y = df["class"].values

# Normalize features
X = (X - X.mean(axis=0)) / X.std(axis=0)


# Initialize Parameters
np.random.seed(42)

input_size = X.shape[1]
hidden_size = 4

W = np.random.randn(hidden_size, input_size) * 0.01
b = np.zeros(hidden_size)

W_out = np.random.randn(hidden_size) * 0.01
b_out = 0.0

# Adam states
m_w = np.zeros_like(W)
v_w = np.zeros_like(W)
m_b = np.zeros_like(b)
v_b = np.zeros_like(b)

m_w_out = np.zeros_like(W_out)
v_w_out = np.zeros_like(W_out)
m_b_out = 0
v_b_out = 0


# Training
epochs = 100
t = 1

for epoch in range(epochs):
    # Forward pass
    Z = np.dot(X, W.T) + b
    H = sigmoid(Z)

    z_out = np.dot(H, W_out) + b_out
    y_hat = sigmoid(z_out)

    # Loss
    loss = binary_cross_entropy(y, y_hat)

    # Backpropagation
    dz_out = y_hat - y

    # Output layer gradients
    dW_out = np.dot(H.T, dz_out) / len(y)
    db_out = np.mean(dz_out)

    # Hidden layer gradients
    dH = dz_out[:, None] * W_out
    dZ = dH * H * (1 - H)

    dW = np.dot(dZ.T, X) / len(X)
    db = np.mean(dZ, axis=0)

    # Adam Updates
    W_out, b_out, m_w_out, v_w_out, m_b_out, v_b_out = adam_update(W_out, b_out, dW_out, db_out,
                                                                   m_w_out, v_w_out, m_b_out, v_b_out, t)

    W, b, m_w, v_w, m_b, v_b = adam_update(W, b, dW, db, m_w, v_w, m_b, v_b, t)
    t += 1

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.6f}")

# Final Evaluation
Z = np.dot(X, W.T) + b
H = sigmoid(Z)

z_out = np.dot(H, W_out) + b_out
y_hat = sigmoid(z_out)

predictions = (y_hat >= 0.5).astype(int)

print("\nFinal Probabilities:\n", y_hat)
print("\nPredictions:\n", predictions)
print("\nActual:\n", y)
