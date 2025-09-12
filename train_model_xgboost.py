import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor
import joblib

# Load your dataset
df = pd.read_csv("train_data.csv")

# Features and target
X = df[["progress", "complexity", "quality", "impact", "timeliness"]]
y = df["score"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define model
model = XGBRegressor(
    n_estimators=100,      # number of boosting rounds
    learning_rate=0.1,     # step size shrinkage
    max_depth=5,           # tree depth
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.2f}, R²: {r2:.2f}")


# Save model to file
model_name = "Model_XGBoost.pkl"
joblib.dump(model, model_name)