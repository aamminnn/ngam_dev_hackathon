import pandas as pd
import joblib
from train_model_svr import mse, r2, model_name
from datetime import datetime

model = joblib.load("Model_SupportVectorRegression.pkl")

new_df = pd.read_csv("test_data.csv")
X_new = new_df[["progress", "complexity", "quality", "impact", "timeliness"]]
new_df["predicted_score"] = model.predict(X_new)

# Rank employees
new_df = new_df.sort_values(by="predicted_score", ascending=False).reset_index(drop=True)
new_df["rank"] = new_df.index + 1

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