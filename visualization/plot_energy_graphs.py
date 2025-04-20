# visualization/plot_energy_graphs.py

import plotly.express as px
import pandas as pd

def plot_clusters(data: pd.DataFrame):
    fig = px.scatter(
        data,
        x='Load(kW)',
        y='EnergyConsumed(kWh)',
        color='EfficiencyGroup',
        symbol='MachineID',
        title="Energy Usage Clustering by Machine",
    )
    return fig
