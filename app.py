# save this as app.py
import streamlit as st
import pandas as pd
import joblib

# Load trained model
clf = joblib.load("Model_XGBoost.pkl")

# Load test data
df = pd.read_csv("test_data.csv")

# Extract features
X_new = df[["progress", "complexity", "quality", "impact", "timeliness"]]

# Predict scores
df["predicted_score"] = clf.predict(X_new)

# Rank employees
df = df.sort_values(by="predicted_score", ascending=False).reset_index(drop=True)

# ----------------- Streamlit UI -----------------
st.title("🏆 Employee Performance Dashboard")

# Show Top 3
st.subheader("🔥 Top 3 Employees")
st.table(df[["emp_name", "predicted_score"]].head(3))

# Show full ranking
st.subheader("📊 Full Ranking")
st.dataframe(df[["emp_name", "predicted_score"]])

# Highlight winner
top_emp = df.iloc[0]
st.success(f"⭐ Best Performer: {top_emp['emp_name']} with score {top_emp['predicted_score']:.2f}")


# What you’ve shown is essentially a styled dashboard UI with:
# Filters (team, role, date range)
# Top contributors card layout with score
# "Why this score" explainability section (showing breakdown of completion, complexity, quality, etc.)
# Trend / summary metrics (time saved, extraction accuracy, agreement score)
# Formula used at the bottom
# Your current Streamlit code can be extended to look like this by:
# Adding filter widgets (dropdowns, date pickers).
# Using card-like layouts with st.columns or community UI components.
# Building an explanation panel per employee, pulling from your calculated metrics.
# Showing summary KPIs at the top using st.metric.
# Using CSS / Streamlit theme to make it colorful and professional.
# So, in short: ✅ Yes, totally possible in Streamlit (or Dash/Gradio if you want alternatives).
# Nabill
