import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Current Customer Analysis")

uploaded_file = st.file_uploader("Upload your customer data (CSV)", type="csv", key="customer")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Customer Data Preview")
    st.dataframe(df)

    # Example Plot 1: Capacity Distribution by Tier
    if "Tier" in df.columns and "Capacity" in df.columns:
        st.subheader("📈 Capacity Distribution by Tier")
        fig1 = px.box(df, x="Tier", y="Capacity", color="Tier")
        st.plotly_chart(fig1, use_container_width=True)

    # Example Plot 2: Number of Customers by Tier
    if "Tier" in df.columns:
        st.subheader("📊 Customer Count by Tier")
        tier_counts = df["Tier"].value_counts().reset_index()
        tier_counts.columns = ["Tier", "Count"]
        fig2 = px.bar(tier_counts, x="Tier", y="Count", color="Tier")
        st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("👆 Upload a CSV with current customer data to view insights.")
