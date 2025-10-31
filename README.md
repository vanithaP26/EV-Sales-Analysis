📊 EV Sales Analysis Project
🔍 Project Overview

The EV Sales Analysis Project focuses on understanding global electric vehicle (EV) sales data through data preprocessing, cleaning, and visualization.
The project includes both Dash (Plotly) and Streamlit dashboards for interactive analysis and reporting.

🧹 Data Processing

Loaded the dataset and handled missing values.

Encoded categorical columns for machine learning compatibility.

Scaled numeric features using StandardScaler.

Detected and removed outliers using the IQR method.

Final clean data reduced from 2360 rows to 1978 rows for better accuracy.

📈 Figure 1: Boxplot before and after cleaning showing the effect of outlier removal.

📉 Dash (Plotly) Dashboard

The Dash dashboard provides an interactive visualization of EV data.
Users can choose:

X-axis and Y-axis variables

Chart types (Line, Bar, Scatter, Histogram, Box)

Key insights:

Analyze sales and growth patterns by year, category, and region.

Real-time updates based on dropdown selections.

Run command:

python plotly.ipynb


(or export as a .py script and run with python filename.py)

🌐 Streamlit Dashboard

The Streamlit dashboard complements the Dash app with a simple web-based interface.
Features include:

CSV file upload

Dataset overview and info

Interactive visualizations (Line, Bar, Scatter, Histogram, Box)

Automatic outlier detection and removal

Run command:

streamlit run stream.py

📁 Project Structure
EV_Sales_Analysis_Project/
│
├── data_preprocessing.ipynb   # Data cleaning and preprocessing
├── plotly.ipynb               # Dash visualization
├── stream.py                  # Streamlit dashboard
├── ev_data_sales.csv          # Dataset
└── README.md                  # Project documentation

⚙️ Requirements

Install dependencies using:

pip install -r requirements.txt


Or manually install:

pandas
numpy
matplotlib
seaborn
plotly
dash
streamlit

🏁 Conclusion

This project demonstrates a complete data analytics pipeline — from data cleaning to interactive dashboard creation.
Both Dash and Streamlit provide visual insights into EV sales trends, making this project useful for data analysis, reporting, and business intelligence.