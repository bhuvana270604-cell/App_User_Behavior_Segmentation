
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="App User Behavior Segmentation",
    page_icon="📊",
    layout="wide"
)

# Load dataset
df = pd.read_csv("app_user_behavior_clustered.csv")

# Title
st.title("📊 App User Behavior Segmentation")

st.write(
    "This dashboard analyzes app user behavior and displays "
    "user segments created using K-Means clustering."
)

# -----------------------------
# Key Metrics
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Users", f"{len(df):,}")

with col2:
    st.metric("Number of Clusters", df["Cluster"].nunique())

with col3:
    st.metric(
        "Average Engagement Score",
        round(df["engagement_score"].mean(), 2)
    )

with col4:
    st.metric(
        "Average Churn Risk",
        round(df["churn_risk_score"].mean(), 2)
    )

# -----------------------------
# Cluster Distribution
# -----------------------------

st.subheader("👥 User Distribution by Cluster")

cluster_counts = df["Cluster"].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(8, 4))

ax.bar(
    cluster_counts.index.astype(str),
    cluster_counts.values
)

ax.set_xlabel("Cluster")
ax.set_ylabel("Number of Users")
ax.set_title("Number of Users in Each Cluster")

st.pyplot(fig)

# -----------------------------
# Cluster Profile
# -----------------------------

st.subheader("📋 Cluster Profile")

profile_columns = [
    "sessions_per_week",
    "daily_active_minutes",
    "engagement_score",
    "churn_risk_score",
    "rating_given",
    "days_since_last_login"
]

cluster_profile = (
    df.groupby("Cluster")[profile_columns]
    .mean()
    .round(2)
)

st.dataframe(cluster_profile)

# -----------------------------
# User Data Preview
# -----------------------------

st.subheader("🔍 User Data")

st.dataframe(df.head(100))
