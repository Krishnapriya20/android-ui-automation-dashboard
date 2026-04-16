import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

# Page config
st.set_page_config(page_title="Automation Dashboard", layout="wide")

# Title
st.title("📊 Automated Member Entry Dashboard")

st.markdown("""
This dashboard displays real-time automation results using ADB-based UI automation.
""")

# Loading effect
with st.spinner("Loading dashboard..."):
    time.sleep(1)

# Load data
try:
    df = pd.read_csv("report.csv")
except:
    st.error("❌ No report.csv found. Run automation first.")
    st.stop()

# Metrics
col1, col2, col3 = st.columns(3)

total = len(df)
success = len(df[df['status'] == "Success"])
fail = len(df[df['status'] == "Fail"])

col1.metric("Total Entries", total)
col2.metric("Success", success)
col3.metric("Failed", fail)

st.divider()

# Chart
st.subheader("📊 Success vs Failure")

status_counts = df['status'].value_counts()

fig, ax = plt.subplots()
ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%')
st.pyplot(fig)

st.divider()

# Filter
st.subheader("🔍 Filter Data")

status_filter = st.selectbox("Filter by Status", ["All", "Success", "Fail"])

if status_filter != "All":
    df = df[df['status'] == status_filter]

# Search
search = st.text_input("Search User")

if search:
    df = df[df['user'].str.contains(search, case=False)]

st.divider()

# Colored table
st.subheader("📋 Entry Details")

def color_status(val):
    if val == "Success":
        return "background-color: lightgreen"
    else:
        return "background-color: lightcoral"

st.dataframe(df.style.applymap(color_status, subset=['status']), use_container_width=True)

# Download button
st.download_button(
    label="📥 Download Report",
    data=df.to_csv(index=False),
    file_name="report.csv",
    mime="text/csv"
)