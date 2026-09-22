# App User Behavior Segmentation

## Project Overview

This project analyzes app user behavior and segments users using K-Means clustering.

The dataset contains 50,000 user records and behavioral features such as sessions per week, daily active minutes, feature clicks, notifications, content downloads, social shares, engagement score and churn risk score.

## Objectives

- Clean and prepare the user behavior dataset
- Perform exploratory data analysis
- Analyze relationships between numerical features
- Standardize numerical features
- Determine the suitable number of clusters using the Elbow Method
- Segment users using K-Means Clustering
- Visualize clusters using PCA
- Build a Streamlit dashboard for user behavior analysis

## Dataset

The dataset contains 50,000 users with 25 features.

Important features include:

- Age
- Gender
- Country
- Device Type
- Sessions per Week
- Average Session Duration
- Daily Active Minutes
- Feature Clicks
- Notifications Opened
- Content Downloads
- Social Shares
- Rating Given
- Churn Risk Score
- Engagement Score
- Account Age
- Marketing Source

## Machine Learning

The project uses:

- StandardScaler for feature scaling
- Elbow Method for selecting K
- K-Means Clustering for user segmentation
- PCA for 2D cluster visualization

The final clustering model contains 4 clusters.

## Streamlit Dashboard

A Streamlit application was created to display:

- Total users
- Number of clusters
- Average engagement score
- Average churn risk
- Cluster distribution
- Cluster profile
- User data

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Google Colab
- GitHub

## Project Files

- `App_User_Behavior_Segmentation.ipynb` — Complete analysis notebook
- `app.py` — Streamlit dashboard
- `app_user_behavior_clustered.csv` — Clustered dataset
- `app_user_behavior_dataset.csv` — Original dataset
- `README.md` — Project documentation

## How to Run

Install the required libraries:

```bash
pip install streamlit pandas matplotlib scikit-learn
