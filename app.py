# ======================================
# WEATHER TEMPERATURE PREDICTION WEB APP
# ======================================

from flask import Flask, render_template, request
import pandas as pd
from glob import glob
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# -------------------------------
# Load and train model (only once)
# -------------------------------

print("Loading dataset...")

files = glob("dataset/*.csv")   # change to *.parquet if needed

df_list = []

for file in files:
    data = pd.read_csv(file)
    df_list.append(data)

df = pd.concat(df_list, ignore_index=True)

df['time'] = pd.to_datetime(df['time'])
df = df.sort_values('time')
df = df.set_index('time')

# Daily temperature
df_daily = df['TMP_2m'].resample('D').mean().dropna()
df_daily = df_daily.to_frame()
df_daily.columns = ['Temperature']

# Convert date to numbers
df_daily['Day_Number'] = range(len(df_daily))

# Train model
model = LinearRegression()
model.fit(df_daily[['Day_Number']], df_daily['Temperature'])

print("Model ready!")

# -------------------------------
# Home Page
# -------------------------------

@app.route('/')
def home():

    # Get latest date from dataset
    last_date = df_daily.index[-1].strftime("%d-%m-%Y")

    return render_template('index.html', last_date=last_date)


# -------------------------------
# Prediction Page
# -------------------------------

@app.route('/predict', methods=['POST'])
def predict():

    days = int(request.form['days'])

    last_day = df_daily['Day_Number'].iloc[-1]

    future_x = pd.DataFrame({
        'Day_Number': range(last_day + 1, last_day + 1 + days)
    })

    prediction = model.predict(future_x)

    # Latest dataset date
    last_date = df_daily.index[-1].strftime("%d-%m-%Y")

    return render_template('index.html',
                           result=f"Predicted temperature for next {days} days: {prediction.mean():.2f} °C",
                           last_date=last_date)


# -------------------------------
# Run App
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True)