import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📈 Sales Prioritization Dashboard")

uploaded_file = st.file_uploader("Upload your company data (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Company Table")
    st.dataframe(df)

    if "Tier" in df.columns and "Capacity" in df.columns and "Assets" in df.columns:
        st.subheader("Tiered Scatter Plot: Assets vs Capacity")
        fig = px.scatter(df, x="Assets", y="Capacity", color="Tier", hover_name="Company name")
        st.plotly_chart(fig)
    else:
        st.warning("Your CSV must include 'Company name', 'Tier', 'Capacity', and 'Assets' columns for the plot.")
else:
    st.info("Please upload a CSV to begin.")
