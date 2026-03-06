import streamlit as st
import pandas as pd
import os
from PIL import Image


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    layout="wide"
)

# =========================
# SIDEBAR NAVIGATION
# =========================
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page:",
    [
        "Profile",
        "Project Overview",
        "Dataset & Preprocessing",
        "Clustering Method",
        "PCA Visualization",
        "Cluster Profile",
        "Cluster Explorer",
        "Recommendation Plan",
        "Limitations"
    ]
)

# =========================
# LOAD DATA
# =========================
# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    file_path = os.path.join("online_retail_cleaned.parquet")

    df = pd.read_parquet(file_path, engine="pyarrow")

    # clean column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    return df


try:
    df = load_data()
except Exception as e:
    st.error(f"Failed to load dataset: {e}")
    st.stop()

# =========================
# CLUSTER SUMMARY DATA
# =========================
cluster_summary = pd.DataFrame({
    "Cluster": [0,1,2,3],
    "Segment": [
        "Dormant Customers",
        "Loyal High-Value Customers",
        "Active Mid-Value Customers",
        "One-Time Customers"
    ],
    "Customers": [1763,1142,1552,1421],
    "Customer Share": ["30.0%","19.4%","26.4%","24.2%"],
    "Recency": ["299 days","18 days","31 days","383 days"],
    "Frequency": ["2 purchases","12.5 purchases","5 purchases","1 purchase"],
    "Monetary": ["$798","$5,599","$1,131","$189"],
    "Revenue Contribution": ["11.0%","75.5%","11.6%","1.9%"],
    "AOV": ["$393.26","$447.58","$231.23","$137.37"],
    "Avg Quantity": ["239 items","267 items","126 items","68 items"]
})

# =========================
# PROFILE PAGE
# =========================
if page == "Profile":

    st.title("About Me")

    col1, col2 = st.columns([1,2])

    with col1:
        image_path = os.path.join("formal_pic.jpg")

        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, width=250)
        else:
            st.warning("Profile image not found.")

    with col2:
        st.subheader("Anthony Djiady Djie")

        st.write("""
        Data Science Bootcamp student at **Dibimbing.id**.

        This project focuses on **Customer Segmentation using K-Means Clustering**
        to understand purchasing behavior and support data-driven marketing strategies.
        """)

        st.markdown("**Tools:** Python, Pandas, Scikit-Learn, Streamlit")

# =========================
# PROJECT OVERVIEW
# =========================
if page == "Project Overview":

    st.title("Project Overview")

    st.subheader("Business Problem")

    st.write("""
    Businesses often treat all customers the same despite differences in purchasing behavior.
    Without segmentation, marketing strategies become inefficient and resources may be wasted.
    """)

    st.subheader("Project Objective")

    st.write("""
    Segment customers using **K-Means clustering** to better understand purchasing behavior
    and support targeted marketing strategies.
    """)

# =========================
# DATASET PAGE
# =========================
if page == "Dataset & Preprocessing":

    st.title("Dataset & Preprocessing")

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    col1,col2,col3 = st.columns(3)

    col1.metric("Total Transactions", len(df))
    col2.metric("Unique Customers", df["customer_id"].nunique())
    col3.metric("Countries", df["country"].nunique())

    st.subheader("Feature Engineering")

    st.write("""
    Customer-level metrics were engineered including:

    - Recency
    - Frequency
    - Monetary
    - Average Order Value (AOV)
    - Average Quantity per Invoice
    """)

# =========================
# CLUSTERING METHOD
# =========================
if page == "Clustering Method":

    st.title("Clustering Method")

    st.write("""
    K-Means clustering was used to segment customers.
    The optimal number of clusters was evaluated using the
    **Elbow Method** and **Silhouette Score**.
    """)

    col1,col2 = st.columns(2)

    with col1:
        st.subheader("Elbow Method")

        elbow_path = os.path.join("elbow_method.png")

        if os.path.exists(elbow_path):
            st.image(elbow_path, use_container_width=True)

    with col2:
        st.subheader("Silhouette Method")

        sil_path = os.path.join("silhouette_method.png")

        if os.path.exists(sil_path):
            st.image(sil_path, use_container_width=True)

    st.info("""
    Although the silhouette score peaks at k=2, k=4 was selected
    because it produces more meaningful customer segments.
    """)

# =========================
# PCA PAGE
# =========================
if page == "PCA Visualization":

    st.title("PCA Visualization")

    st.write("""
    PCA was used to visualize customer clusters in two dimensions.
    """)

    pca_path = os.path.join("assets","PCA final.png")

    if os.path.exists(pca_path):
        st.image(pca_path, use_container_width=True)

# =========================
# CLUSTER PROFILE
# =========================
if page == "Cluster Profile":

    st.title("Cluster Profile Overview")

    st.dataframe(cluster_summary, use_container_width=True)

# =========================
# CLUSTER EXPLORER
# =========================
if page == "Cluster Explorer":

    st.title("Cluster Explorer")

    selected = st.selectbox(
        "Select Cluster",
        ["Cluster 0","Cluster 1","Cluster 2","Cluster 3"]
    )

    cluster_num = int(selected.split()[1])

    row = cluster_summary[cluster_summary["Cluster"] == cluster_num]

    st.dataframe(row, use_container_width=True)

# =========================
# RECOMMENDATION PLAN
# =========================
if page == "Recommendation Plan":

    st.title("1-Month Recommendation Plan")

    plan = pd.DataFrame({
        "Week":[
            "Week 1",
            "Week 2",
            "Week 3",
            "Week 4"
        ],
        "Focus":[
            "Campaign Preparation",
            "Retain High-Value Customers",
            "Grow Mid-Value Customers",
            "Reactivate Inactive Customers"
        ],
        "Action":[
            "Prepare segmented customer lists",
            "Launch loyalty and VIP programs",
            "Upselling and bundle promotions",
            "Reactivation campaigns"
        ]
    })

    st.dataframe(plan, use_container_width=True)

# =========================
# LIMITATIONS
# =========================
if page == "Limitations":

    st.title("Project Limitations")

    st.write("""
    - No demographic data available
    - No marketing campaign interaction data
    - No profit or margin information
    - Only transaction behavior was analyzed
    """)

    st.write("""
    Future improvements may include demographic,
    marketing response, and behavioral engagement data.

    """)


