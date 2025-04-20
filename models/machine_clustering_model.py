# models/machine_clustering_model.py

import pandas as pd
from sklearn.cluster import KMeans

def cluster_machines(data: pd.DataFrame, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    data['EfficiencyGroup'] = kmeans.fit_predict(data[['Load(kW)', 'EnergyConsumed(kWh)']])
    return data, kmeans
