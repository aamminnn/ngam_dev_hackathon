import pandas as pd
from train_model_linearregression import mse,r2,model_name
from datetime import datetime
import joblib

# Load trained model
model = joblib.load("Model_LinearRegression.pkl")

# Load new employee data
new_df = pd.read_csv("test_data.csv")

# Extract features
X_new = new_df[["progress", "complexity", "quality", "impact", "timeliness"]]

# Predict performance scores
new_df["predicted_score"] = model.predict(X_new)

# Rank employees
new_df = new_df.sort_values(by="predicted_score", ascending=False).reset_index(drop=True)
new_df["rank"] = new_df.index + 1

print(new_df[["rank", "emp_name", "predicted_score"]])

# Example evaluation metrics (dummy here, replace with your real eval result)
mse = mse
r2 = r2
model_name = model_name

# Save log with DataFrame output
with open("logs/model_logs.log", "a") as f:
    f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Model={model_name} | MSE={mse:.2f} | R2={r2:.2f}\n")
    f.write("Employee Rankings:\n")
    f.write(new_df[["rank", "emp_name", "predicted_score"]].to_string(index=False))
    f.write("\n" + "-"*50 + "\n")
print("Log updated successfully!")
print(new_df[["emp_name", "predicted_score"]])
