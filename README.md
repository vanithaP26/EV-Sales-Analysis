# ⚡ EV Sales Analysis Project

## 📘 Overview
The **EV Sales Analysis Project** explores global Electric Vehicle (EV) sales data through data preprocessing, cleaning, and visualization.  
It includes two interactive dashboards built using **Dash (Plotly)** and **Streamlit**, providing user-friendly tools for data analysis and business intelligence.

---

## 🧹 Data Processing
The dataset was cleaned and prepared before visualization.

### Steps Performed
- Loaded and inspected the dataset (`ev_data_sales.csv`)
- Handled missing values
- Encoded categorical columns
- Scaled numeric features using *StandardScaler*
- Removed outliers using the *IQR method*
- Final clean dataset reduced from **2360 → 1978 rows**

---

## 📉 Dash (Plotly) Dashboard

### Features
- Choose X-axis and Y-axis columns dynamically  
- Select chart type (Line, Bar, Scatter, Histogram, Box)  
- Interactive charts using dropdown filters  

### Run Command
```bash
python plotly.ipynb
```bash


🌐 Streamlit Dashboard
Features
Dataset overview and info

Interactive visualizations (Line, Bar, Scatter, Histogram, Box)

Automatic outlier detection and removal

Run Command
```bash
streamlit run stream.py
```bash

📁 Project Structure
```bash

EV_Sales_Analysis_Project/
│
├── data_preprocessing.ipynb   # Data cleaning and preprocessing
├── plotly.ipynb               # Dash visualization
├── stream.py                  # Streamlit dashboard
├── ev_data_sales.csv          # Dataset
└── README.md                  # Project documentation
```bash

⚙️ Requirements
Install dependencies using:

```bash
pip install -r requirements.txt
```bash

Or manually install:

```bash
pandas
numpy
matplotlib
seaborn
plotly
dash
streamlit
```bash

🏁 Conclusion
This project demonstrates a complete data analytics pipeline — from data cleaning to interactive dashboard creation.
Both Dash and Streamlit provide visual insights into EV sales trends, making this project useful for data analysis, reporting, and business intelligence.

👩‍💻 Author
Vanitha P
📍 EV Sales Analysis Project | 2025

