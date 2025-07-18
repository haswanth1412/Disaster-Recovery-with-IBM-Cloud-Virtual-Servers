import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(df):
    features = ['population_density', 'infrastructure_score', 'previous_disasters', 'alert_level']
    scaler = StandardScaler()
    X = scaler.fit_transform(df[features])
    return X
