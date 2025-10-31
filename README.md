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

### ▶️ Run Command
Run the Dash visualization from the notebook or export it as a `.py` file:

```bash
python plotly.ipynb

---

```markdown
## 🌐 Streamlit Dashboard

### Features
- Dataset overview and info  
- Interactive visualizations (Line, Bar, Scatter, Histogram, Box)  
- Automatic outlier detection and removal  

### ▶️ Run Command
To launch the interactive Streamlit dashboard, use:

```bash
streamlit run stream.py
