import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from utils.preprocess import load_and_preprocess_data
import sqlite3

model = load_model('model/dnn_disaster_model.h5')

conn = sqlite3.connect('database/recovery_zones.db')
df = pd.read_sql_query("SELECT * FROM disaster_data", conn)
conn.close()

X = load_and_preprocess_data(df)

predictions = model.predict(X)
df['ImpactScore'] = predictions

print("Top 5 High-Risk Zones:")
print(df.sort_values(by='ImpactScore', ascending=False).head())
