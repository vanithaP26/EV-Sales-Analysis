📊 EV Sales Data Analysis Dashboard

An interactive data visualization and analytics project built using Python, Pandas, Plotly, and Streamlit to explore and analyze Electric Vehicle (EV) Sales Data.

🚀 Project Overview

The project focuses on data preprocessing, exploration, and visualization of EV sales trends to help understand growth patterns and insights in the electric vehicle market.

🧠 Key Features

📈 Cleaned and preprocessed raw EV sales data

🧹 Handled missing values and performed data transformation

📊 Interactive visualizations using Plotly

🧭 Streamlit dashboard for user interaction

📅 Analysis by year, region, and vehicle type

🎯 Detection and removal of outliers

📁 Supports multiple chart types (Line, Bar, Scatter, Histogram, Box)

🧩 Technologies Used
Category	Tools / Libraries
Language	Python
Data Processing	Pandas, NumPy
Visualization	Plotly, Matplotlib, Seaborn
Dashboard	Streamlit
IDE Used	Jupyter Notebook, Visual Studio Code
⚙️ Installation & Requirements

Install the following Python packages before running:

pip install pandas numpy matplotlib seaborn plotly streamlit

🗂️ Project Structure
📁 EV_Sales_Analysis_Project
│
├── 📄 ev_data_preprocessing.ipynb     # Data cleaning and preprocessing
├── 📄 plotly.ipynb                    # Data visualization notebook
├── 📄 stream.py                       # Streamlit dashboard script
├── 📄 dataset.csv                     # EV Sales dataset
└── 📄 README.md                       # Project documentation

🔍 Data Preprocessing

Performed using Jupyter Notebook:

Loaded dataset using Pandas

Checked for null or duplicate values

Removed or imputed missing data

Converted data types

Performed feature selection and basic statistics

Saved cleaned data for visualization

Example code snippet:

import pandas as pd

df = pd.read_csv("EV_sales.csv")
df.info()
df.describe()
df.dropna(inplace=True)
df.to_csv("Cleaned_EV_Sales.csv", index=False)

📊 Visualization (Plotly)

Created multiple visualizations using Plotly Express:

import plotly.express as px

df = px.data.iris()  # Example dataset
fig = px.bar(df, x="sepal_width", y="sepal_length", color="species", barmode="group")
fig.show()

🌐 Streamlit Dashboard

The Streamlit app allows users to interactively explore and visualize EV data.

Features

Dataset overview and summary

Interactive visualizations (Line, Bar, Scatter, Histogram, Box)

Dynamic dropdown filters

Outlier detection and removal

▶️ Run Command

Run the dashboard using:

streamlit run stream.py


To open the notebook version, run:

python plotly.ipynb

📸 Example Dashboard Output

Add your dashboard screenshots here for better presentation (optional).

🧾 Conclusion

This project successfully demonstrates the complete data analysis workflow — from data preprocessing to interactive dashboard visualization.
It helps users gain insights into EV market trends, growth, and data patterns through clean visuals and analysis.

👩‍💻 Author

Developed by Vanitha P
📬 GitHub: vanithaP26