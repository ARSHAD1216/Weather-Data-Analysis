Weather-Data-Analysis

This project is a Weather Data Analysis and Prediction Web App for Tamil Nadu, India (2019–2024). The app predicts weather parameters and displays the results through a web interface built with Flask.

Project Structure
Weather-Data-Analysis/
│
├── app.py                  # Main Flask application
├── templates/
│   └── index.html          # Web page template
├── dataset/                # Folder containing CSV files (not included in GitHub)
│   ├── Weather_Final_data_2019_imputed.csv
│   ├── Weather_Final_data_2020_imputed.csv
│   ├── Weather_Final_data_2021_imputed.csv
│   ├── Weather_Final_data_2022_imputed.csv
│   ├── Weather_Final_data_2023_imputed.csv
│   └── Weather_Final_data_2024_imputed.csv
├── requirements.txt        # Python dependencies
└── README.md               # Project description
Important Note

The dataset folder is NOT included in this GitHub repository due to size constraints.

To run the project locally, you need to have the CSV files for the years 2019–2024 inside a folder named dataset in the project root.

How to Run the Project Locally
Clone the repository:
git clone https://github.com/Arshad1216/Weather-Data-Analysis.git
cd Weather-Data-Analysis
Install dependencies:
pip install -r requirements.txt
Make sure the dataset folder with all CSV files is inside the project directory.
Run the Flask app:
python app.py
Open your browser and go to:
http://127.0.0.1:5000
