# =====================================
# WEATHER DATA ANALYSIS AND PREDICTION
# =====================================

print("Loading dataset...")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

# =====================================
# 1. LOAD ALL FILES FROM DATASET FOLDER
# =====================================

files = glob("dataset/*.csv")   # change to *.parquet if your files are parquet

df_list = []

for file in files:
    data = pd.read_csv(file)
    df_list.append(data)

df = pd.concat(df_list, ignore_index=True)

print("Dataset loaded successfully!")
print("Total rows:", len(df))

# =====================================
# 2. CONVERT TIME COLUMN
# =====================================

df['time'] = pd.to_datetime(df['time'])
df = df.sort_values('time')
df = df.set_index('time')

print("Data range:")
print(df.index.min())
print(df.index.max())

print(df.head())

# =====================================
# 3. TEMPERATURE TREND GRAPH
# =====================================

print("Creating temperature trend graph...")

df_daily = df['TMP_2m'].resample('D').mean()

plt.figure(figsize=(15,6))
plt.plot(df_daily)

plt.title("Daily Average Temperature Trend (2019–2024)")
plt.xlabel("Year")
plt.ylabel("Temperature at 2m (°C)")
plt.grid(True)

plt.show()

# =====================================
# 4. PREPARE DATA FOR PREDICTION
# =====================================

print("Preparing data for prediction...")

# Select useful features
features = ['RH_2m','VIS_2m','UGRD_10m','VGRD_10m','PRES_sfc','APCP_sfc']
target = 'TMP_2m'

df_model = df[features + [target]].dropna()

X = df_model[features]
y = df_model[target]

# =====================================
# 5. TRAIN TEST SPLIT
# =====================================

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =====================================
# 6. TRAIN MODEL
# =====================================

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

print("Model trained successfully!")

# =====================================
# 7. PREDICTION
# =====================================

y_pred = model.predict(X_test)

# =====================================
# 8. ACCURACY CHECK
# =====================================

from sklearn.metrics import mean_absolute_error, r2_score

print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

print("Project completed successfully!")