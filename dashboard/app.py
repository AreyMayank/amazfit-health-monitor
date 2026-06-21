"""
Amazfit Health Dashboard

Displays collected smartwatch data.
"""


import streamlit as st

import pandas as pd

import os



DATA_FILE = (
    "data/health_data.csv"
)



st.set_page_config(

    page_title="Amazfit Health Monitor",

    layout="wide"

)



st.title(
    "⌚ Amazfit Health Monitor"
)



if not os.path.exists(
    DATA_FILE
):

    st.warning(
        "No health data available yet"
    )

    st.stop()



data = pd.read_csv(
    DATA_FILE
)



latest = data.iloc[-1]



col1, col2, col3, col4 = st.columns(
    4
)



with col1:

    st.metric(
        "🔋 Battery",
        f"{latest['battery']}%"
    )



with col2:

    st.metric(
        "❤️ Heart Rate",

        latest["heart_rate"]
        if pd.notna(
            latest["heart_rate"]
        )
        else "Waiting"
    )



with col3:

    st.metric(
        "🚶 Steps",

        latest["steps"]
        if pd.notna(
            latest["steps"]
        )
        else "Waiting"
    )



with col4:

    st.metric(
        "🫁 SpO2",

        latest["spo2"]
        if pd.notna(
            latest["spo2"]
        )
        else "Waiting"
    )



st.subheader(
    "Battery Trend"
)



st.line_chart(

    data,

    x="timestamp",

    y="battery"

)



st.subheader(
    "Raw Health Data"
)


st.dataframe(
    data
)