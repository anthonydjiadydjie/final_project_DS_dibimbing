Customer Segmentation Dashboard

Interactive Streamlit dashboard for exploring customer segmentation using K-Means clustering based on purchasing behavior.

This dashboard was built as part of a Data Science final project to analyze customer transaction data and support targeted marketing strategies.

Overview

The dashboard visualizes customer segments created using K-Means clustering based on behavioral features such as:

Recency (how recently a customer purchased)

Frequency (how often they purchase)

Monetary value (how much they spend)

Average Order Value

Average Quantity per Invoice

These metrics help identify different customer groups and provide actionable business insights.

Dashboard Features

The Streamlit app includes multiple pages:

Profile – Author information

Project Overview – Business problem and objectives

Dataset & Preprocessing – Dataset summary and metrics

Clustering Method – Explanation of K-Means, Elbow, and Silhouette methods

PCA Visualization – Cluster visualization in reduced dimensions

Cluster Profile – Summary of customer segments

Cluster Explorer – Interactive cluster exploration

Recommendation Plan – Business strategies based on clusters

Limitations – Project constraints and future improvements

Project Structure
customer-segmentation-dashboard
│
├── app.py
├── README.md
├── requirements.txt
│
├── data
│   └── online_retail_cleaned.parquet
│
├── assets
│   ├── elbow_method.png
│   ├── silhouette_method.png
│   ├── PCA final.png
│   └── formal_pic.jpg
Installation

Clone the repository:

git clone https://github.com/anthonydjiadydjie/customer-segmentation-dashboard.git
cd customer-segmentation-dashboard

Install dependencies:

pip install -r requirements.txt
Run the Streamlit App

Start the dashboard locally:

streamlit run app.py

The app will open in your browser at:

http://localhost:8501
Dataset

The dataset used in this project comes from the Online Retail II dataset, which contains transaction data from a UK-based online retailer.

The dataset was cleaned and transformed into a Parquet file for faster loading in the Streamlit dashboard.

Technologies Used

Python

Pandas

Scikit-learn

Streamlit

PyArrow

Author

Anthony Djiady Djie
Data Science Bootcamp – Dibimbing.id

LinkedIn
https://www.linkedin.com/in/anthony-djiady-djie
