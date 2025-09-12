import pandas as pd
import joblib
import logging
from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("train_data.csv")

X = df[["progress", "complexity", "quality", "impact", "timeliness"]]
y = df["score"]   # your target column

# ==============================
# Train SVR model
# ==============================
svr_model = SVR(kernel="rbf", C=100, epsilon=5)  # you can tweak params
svr_model.fit(X, y)

# ==============================
# Evaluate Model
# ==============================
predictions = svr_model.predict(X)
r2 = r2_score(y, predictions)
mse = mean_squared_error(y, predictions)

print(f"MSE: {mse:.2f}, R²: {r2:.2f}")

# Save model for future use
model_name =  "Model_SupportVectorRegression.pkl"
joblib.dump(svr_model, model_name)
