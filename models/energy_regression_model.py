# models/energy_regression_model.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

def train_energy_model(data: pd.DataFrame, use_xgb=False):
    X = data[['Load(kW)', 'OperationTime(min)']]
    y = data['EnergyConsumed(kWh)']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = XGBRegressor() if use_xgb else LinearRegression()
    model.fit(X_train, y_train)
    return model
