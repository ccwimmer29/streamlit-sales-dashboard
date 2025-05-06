import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Config ---
st.set_page_config(page_title="Amperon 1000 Dashboard", layout="wide")

# --- Amperon Logo + Custom Title ---
st.markdown(
    """
    <div style='text-align: center;'>
        <img src='https://github.com/ccwimmer29/streamlit-sales-dashboard/blob/main/avatar.png?raw=true' width='200'/>
        <h1 style='color: #054A91; font-size: 3em; margin-bottom: 0;'>⚡️ Welcome to the Amperon 1000 ⚡️</h1>
        <p style='color: #3E7CB1; font-size: 1.2em;'>Smart Sales Prioritization for the Energy Future</p>
        <hr style="border: 1px solid #7DC1F1; width: 80%; margin: auto;" />
    </div>
    """,
    unsafe_allow_html=True
)

# --- File Upload ---
uploaded_file = st.file_uploader("📤 Upload your company data (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📋 Company Table")
    st.dataframe(df)

    # --- Scatter Plot ---
    if "Tier" in df.columns and "Capacity" in df.columns and "Assets" in df.columns:
        st.subheader("📈 Tiered Scatter Plot: Assets vs Capacity")

        amperon_colors = {
            "Tier 1": "#054A91",  # Dark Blue
            "Tier 2": "#3E7CB1",  # Medium Blue
            "Tier 3": "#7DC1F1"   # Light Blue
        }

        fig = px.scatter(
            df,
            x="Assets",
            y="Capacity",
            color="Tier",
            hover_name="Company name",
            color_discrete_map=amperon_colors
        )

        fig.update_layout(
            plot_bgcolor="#F8F9FA",
            paper_bgcolor="#F8F9FA",
            font=dict(color="#363840")
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Your CSV must include 'Company name', 'Tier', 'Capacity', and 'Assets' columns for the plot.")
else:
    st.info("👆 Please upload a CSV to begin.")

