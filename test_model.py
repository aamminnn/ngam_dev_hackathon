import pandas as pd
import joblib

# Load trained model
clf = joblib.load("performance_model.pkl")

# Load new dataset
new_df = pd.read_csv("test_data.csv")

# Extract features
X_new = new_df[["progress", "complexity", "quality", "impact", "timeliness"]]

# Predict scores
new_df["predicted_score"] = clf.predict(X_new)

# Rank employees
new_df = new_df.sort_values(by="predicted_score", ascending=False).reset_index(drop=True)

print(new_df[["emp_name", "predicted_score"]])
