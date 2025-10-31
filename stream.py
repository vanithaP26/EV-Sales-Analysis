import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Smart Dataset Visualization App", layout="wide")
st.title("Interactive Data Visualization Dashboard")

st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)
    st.success("✅ File Uploaded Successfully!")

    # Dataset Overview
    st.subheader(" Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)
    st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
    st.write("**Columns:**", list(df.columns))

    # ======================================
    # Identify Column Types
    # ======================================
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    with st.expander(" Dataset Information"):
        st.write("**Numeric Columns:**", num_cols)
        st.write("**Categorical Columns:**", cat_cols)

    # ======================================
    #  Visualization Controls
    # ======================================
    st.sidebar.header("🎛 Visualization Options")
    chart_type = st.sidebar.selectbox(
        "Choose Chart Type",
        ["Line Chart", "Bar Chart", "Scatter Plot", "Histogram", "Box Plot"]
    )

    # Auto-detect valid columns
    if chart_type in ["Line Chart", "Bar Chart", "Scatter Plot"]:
        if len(num_cols) >= 2:
            x_col = st.sidebar.selectbox("Select X-axis", df.columns)
            y_col = st.sidebar.selectbox("Select Y-axis", num_cols)
        else:
            st.warning("⚠️ Please upload a dataset with at least two numeric columns.")
            st.stop()
    elif chart_type in ["Histogram", "Box Plot"]:
        y_col = st.sidebar.selectbox("Select Column", num_cols)
        x_col = None

    # ======================================
    # Generate Visualization
    # ======================================
    st.subheader(f"📈 {chart_type}")

    fig, ax = plt.subplots(figsize=(8, 5))

    try:
        if chart_type == "Line Chart":
            ax.plot(df[x_col], df[y_col], marker='o')
            ax.set_title(f"{y_col} vs {x_col}")

        elif chart_type == "Bar Chart":
            df_sample = df[[x_col, y_col]].dropna().head(30)
            ax.bar(df_sample[x_col].astype(str), df_sample[y_col])
            ax.tick_params(axis='x', rotation=45)
            ax.set_title(f"{y_col} by {x_col}")

        elif chart_type == "Scatter Plot":
            ax.scatter(df[x_col], df[y_col], alpha=0.7, color='teal')
            ax.set_title(f"{y_col} vs {x_col}")

        elif chart_type == "Histogram":
            ax.hist(df[y_col], bins=25, color='orange', edgecolor='black')
            ax.set_title(f"Distribution of {y_col}")

        elif chart_type == "Box Plot":
            # --- Detect & Remove Outliers using IQR ---
            Q1 = df[y_col].quantile(0.25)
            Q3 = df[y_col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            outliers = df[(df[y_col] < lower_bound) | (df[y_col] > upper_bound)]
            df_no_outliers = df[(df[y_col] >= lower_bound) & (df[y_col] <= upper_bound)]

            ax.boxplot(df_no_outliers[y_col], patch_artist=True)
            ax.set_title(f"Box Plot of {y_col} (Outliers Removed)")
            

        ax.set_xlabel(x_col if x_col else "")
        ax.set_ylabel(y_col)
        ax.grid(True, linestyle='--', alpha=0.5)

        st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Error generating plot: {e}")

else:
    st.info("📂 Please upload a CSV file to begin visualizing your dataset.")
