# app.py

import streamlit as st
from utils.data_loader import load_and_preprocess
from models.energy_regression_model import train_energy_model
from models.machine_clustering_model import cluster_machines
from visualization.plot_energy_graphs import plot_clusters
from utils.scheduler_utils import suggest_optimal_load

# Title
st.title("⚙️ Energy Consumption Optimization in Smart Factories")

# Load and preprocess data
data = load_and_preprocess("data/sample_energy_data.csv")

# Cluster Machines
st.subheader("🔍 Efficiency Clustering of Machines")
clustered_data, kmeans_model = cluster_machines(data)
st.plotly_chart(plot_clusters(clustered_data))

# Prediction
st.subheader("📈 Energy Consumption Prediction")
load = st.slider("Machine Load (kW)", 10, 100, 50)
op_time = st.slider("Operation Time (min)", 10, 120, 60)
model_type = st.selectbox("Choose Model", ["Linear Regression", "XGBoost"])

model = train_energy_model(data, use_xgb=(model_type == "XGBoost"))
predicted_energy = model.predict([[load, op_time]])[0]
st.success(f"Predicted Energy: {predicted_energy:.2f} kWh")

# Time-based Suggestion
st.subheader("⏳ Optimized Load Suggestion")
slot = st.selectbox("Select Time Slot", ["Morning", "Afternoon", "Evening"])
suggested = suggest_optimal_load(slot, load)
st.info(f"Suggested Load: {suggested} kW for {slot} operation")
