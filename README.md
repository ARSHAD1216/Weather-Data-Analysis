# Weather-Data-Analysis

This project is a **Weather Data Analysis and Prediction** application for Tamil Nadu, India, covering the years **2019-2024**. The application loads multiple weather datasets, performs preprocessing, trains a prediction model, and provides an interactive web interface for predicting weather conditions.

---

## ⚡ Features

- Loads weather data for Tamil Nadu from 2019 to 2024.
- Preprocesses data for machine learning tasks.
- Trains a regression model for weather prediction.
- Provides a **web-based interface** to enter date and location to predict weather.
- Displays current dataset date on the web page.

---

## 📂 Dataset

The datasets used are **not included in this repository** due to size limitations.  
You will need to download or prepare the following CSV files and place them inside a folder named `dataset` in the project root:

- `Weather_Final_data_2019_imputed.csv`
- `Weather_Final_data_2020_imputed.csv`
- `Weather_Final_data_2021_imputed.csv`
- `Weather_Final_data_2022_imputed.csv`
- `Weather_Final_data_2023_imputed.csv`
- `Weather_Final_data_2024_imputed.csv`

Directory structure:


Weather-Data-Analysis/
├─ app.py
├─ templates/
│ └─ index.html
├─ dataset/
│ ├─ Weather_Final_data_2019_imputed.csv
│ ├─ Weather_Final_data_2020_imputed.csv
│ └─ ... (all other years)
├─ requirements.txt
└─ README.md


---

## 💻 How to Run

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/Weather-Data-Analysis.git
Install required packages:
pip install -r requirements.txt
Run the application:
python app.py
Open your browser and go to:
http://127.0.0.1:5000
Enter date and location to predict weather.
