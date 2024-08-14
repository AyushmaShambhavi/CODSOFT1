import streamlit as st
import pandas as pd 
import time
from datetime import datetime

# Get current date and time
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")

# Construct the file path for today's attendance CSV
csv_file_path = f"Attendance/Attendance_{date}.csv"

# Check if the CSV file exists
try:
    df = pd.read_csv(csv_file_path)
    st.dataframe(df.style.highlight_max(axis=0))
except FileNotFoundError:
    st.error(f"File not found: {csv_file_path}")
