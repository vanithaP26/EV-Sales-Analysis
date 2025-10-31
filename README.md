# ⚡ Electric Vehicle (EV) Sales Analysis Dashboard

A complete data analysis and visualization project built using **Python, Pandas, Matplotlib, and Streamlit**, showcasing insights from global EV sales data.

---

## 🧩 Project Overview
This project analyzes **Electric Vehicle (EV) sales trends** across various regions and years, providing insights into adoption growth, manufacturer performance, and market patterns.

The dashboard is built using **Streamlit** for interactive visualization and data exploration.

---

## 📁 Project Structure
```
EV_Sales_Analysis_Project/
│
├── data/
│   └── IEA-EV-dataEV salesHistoricalCars.csv
│
├── EV_Data_Preprocessing.ipynb        # Data cleaning and preprocessing
├── EV_Dashboard.py                    # Streamlit dashboard code
├── README.md                          # Project documentation
└── outputs                            # images 

```

## ⚙️ Technologies Used

- **Python 3**
- **Pandas** – Data manipulation
- **Matplotlib / Plotly** – Visualization
- **Streamlit** – Interactive dashboard
- **Jupyter Notebook** – Data preprocessing

---

## 🧠 Key Features
✅ Data cleaning and preprocessing using Pandas  
✅ Visualization of EV sales trends by country, company, and year  
✅ Interactive Streamlit dashboard for dynamic insights  
✅ Ready-to-run deployment setup

---

## 🧹 Data Preprocessing Steps
1. **Import Dataset**
   ```python
   import pandas as pd
   df = pd.read_csv('EV_sales_data.csv')
2. **Handle Missing Values**
   ```python
   df = df.dropna()
3. **Convert Data Types**
   ```python
   df['Year'] = df['Year'].astype(int)
4. **Basic Analysis**
   ```python
   df.describe()
   df.info()

📊 Dashboard (Streamlit)
File: ev_dashboard.py

Example Code
```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="EV Sales Dashboard", layout="wide")

df = pd.read_csv("data/EV_sales_data.csv")

st.title("⚡ EV Sales Analysis Dashboard")

col1, col2 = st.columns(2)
with col1:
    country = st.selectbox("Select Country", df["Country"].unique())
with col2:
    year = st.slider("Select Year", int(df["Year"].min()), int(df["Year"].max()), int(df["Year"].min()))

filtered_df = df[(df["Country"] == country) & (df["Year"] == year)]

fig = px.bar(filtered_df, x="Manufacturer", y="Sales", color="Manufacturer",
             title=f"EV Sales by Manufacturer in {country} ({year})")
st.plotly_chart(fig, use_container_width=True)

```
👩‍💻 Author

Vanitha P

📧 vanithavani.p26@gmail.com

🔗 https://github.com/vanithaP26

