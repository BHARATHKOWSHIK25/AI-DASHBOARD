"""
Supermarket Sales Dashboard
A Streamlit dashboard that visualizes supermarket sales data with KPI metrics
and an interactive revenue chart by product line.

Dataset: Supermarket Sales (sales.csv)
Run: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.express as px

# ── Page Config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# ── Load Data ──────────────────────────────────────────────────────────────────
df = pd.read_csv("sales.csv")

# ── Title ──────────────────────────────────────────────────────────────────────
st.title("📊 Supermarket Sales Dashboard")

# ── KPI Metrics ────────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)

col1.metric(
    label="💰 Total Revenue",
    value=f"${df['Total'].sum():,.2f}"
)

col2.metric(
    label="🛒 Total Quantity Sold",
    value=int(df['Quantity'].sum())
)

col3.metric(
    label="⭐ Average Rating",
    value=round(df['Rating'].mean(), 2)
)

# ── Dataset Preview ────────────────────────────────────────────────────────────
st.subheader("Dataset Preview")
st.dataframe(df.head())

# ── Revenue by Product Line Chart ─────────────────────────────────────────────
revenue = (
    df.groupby("Product line")["Total"]
    .sum()
    .reset_index()
)

fig = px.bar(
    revenue,
    x="Product line",
    y="Total",
    title="Revenue by Product Line",
    labels={"Total": "Total Revenue ($)", "Product line": "Product Line"},
    color="Product line",
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig.update_layout(showlegend=False)
st.plotly_chart(fig, use_container_width=True)
