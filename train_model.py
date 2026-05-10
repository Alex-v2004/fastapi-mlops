from sklearn.linear_model import LinearRegression
import numpy as np
import joblib

# Training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([35, 45, 55, 65, 75])

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "/model.pkl")

print("Model trained and saved!")