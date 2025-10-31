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
(or export notebook to .py and run)

🌐 Streamlit Dashboard
Features
Dataset overview and info

Interactive visualizations (Line, Bar, Scatter, Histogram, Box)

Automatic outlier detection and removal

Run Command
bash
Copy code
streamlit run stream.py
📁 Project Structure
bash
Copy code
EV_Sales_Analysis_Project/
│
├── data_preprocessing.ipynb   # Data cleaning and preprocessing
├── plotly.ipynb               # Dash visualization
├── stream.py                  # Streamlit dashboard
├── ev_data_sales.csv          # Dataset
└── README.md                  # Project documentation
⚙️ Requirements
Install dependencies using:

bash
Copy code
pip install -r requirements.txt
Or manually install:

bash
Copy code
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

👩‍💻 Author
Vanitha P
📍 EV Sales Analysis Project | 2025

yaml
Copy code

---

### 💡 Now do this:
1. Replace your current README text with the one above.  
2. Save it as `README.md` (not `.txt`).  
3. Run:
   ```bash
   git add README.md
   git commit -m "Fix README formatting"
   git push