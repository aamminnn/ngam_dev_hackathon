import pandas as pd
from datasets import load_dataset
from tabpfn import TabPFNClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import joblib

# Load your CSV into HuggingFace Dataset
dataset = load_dataset("csv", data_files="train_data.csv")

# Train/Test split
train_test = dataset["train"].train_test_split(test_size=0.2)
train = train_test["train"]
test = train_test["test"]

# Extract features + labels
X_train = [ [r["progress"], r["complexity"], r["quality"], r["impact"], r["timeliness"]] for r in train ]
y_train = [ r["score"] for r in train ]

X_test = [ [r["progress"], r["complexity"], r["quality"], r["impact"], r["timeliness"]] for r in test ]
y_test = [ r["score"] for r in test ]

# Train TabPFN
# clf = TabPFNClassifier(N_ensemble_configurations=32)
clf = RandomForestRegressor(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
# print("Accuracy:", clf.score(X_test, y_test))
preds = clf.predict(X_test)
mse = mean_squared_error(y_test, preds)
print("MSE:", mse)
r2 = r2_score(y_test, preds)
print("R²:", r2)

# Save model to file
model_name = "RandomForest.pkl"
joblib.dump(clf, model_name)