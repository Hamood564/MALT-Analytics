import time
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import malt_apiWrapper as malt
import json,re
from io import StringIO


BASE_URL = "http://localhost:8086/api/malt"  # Java Web API

st.set_page_config(page_title="MALT Analytics", layout="wide")
st.title("🧪 MALT Data Analytics Frontend")

st.sidebar.header("Test Control Panel")

# Input fields
ip = st.sidebar.text_input("MALT IP Address", "192.168.115.177")
test_index = st.sidebar.number_input("Test Index", min_value=0, max_value=15, value=2)

# Start Test
if st.sidebar.button("▶️ Start Test"):
    with st.spinner("Running test on MALT... please wait..."):
        # Start the test
        response = malt.start_test(ip, test_index)
        st.info("Test command sent. Waiting for completion...")

        # Poll the status every second
        timeout = 60  # max wait 60 seconds
        for _ in range(timeout):
            if not malt.is_test_running(ip):
                break
            time.sleep(1)

        st.success("Test completed ✅")

        # Show result code
        result_code = malt.get_result_code(ip)
        st.subheader("Result Code:")
        st.code(result_code)

        # Show last data
        last_data = malt.get_last_data(ip)
        st.subheader("Test Data:")
        st.text_area("Raw Data", last_data, height=200)

        try:
            clean_json = re.sub(r"[\x00-\x1F\x7F]", "", last_data)
            data_dict = json.loads(clean_json)
            message_csv = data_dict['response']['message']

            csv_io = StringIO(message_csv)
            df_last = pd.read_csv(csv_io)

            # Clean and fix columns
            df_last.columns = [col.strip().replace("\r", "") for col in df_last.columns]
            st.write("Detected columns:", df_last.columns.tolist())

            if df_last.shape[1] == 4:
                df_last.columns = ["Step", "Time(ms)", "Test Pres", "Diff Pres"]

            # Plot
            st.subheader("📊 Test Pressure & Diff Pressure")
            fig, ax = plt.subplots()
            ax.plot(df_last["Time(ms)"], df_last["Test Pres"], label="Test Pressure")
            ax.plot(df_last["Time(ms)"], df_last["Diff Pres"], label="Diff Pressure")
            ax.set_xlabel("Time (ms)")
            ax.set_ylabel("Pressure")
            ax.legend()
            st.pyplot(fig)

            # Table
            st.subheader("🧾 Data Preview")
            st.dataframe(df_last.head(20))

            # Download
            st.download_button(
                label="💾 Download CSV",
                data=df_last.to_csv(index=False).encode('utf-8'),
                file_name="last_test_data.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"Error parsing last-data JSON: {e}")


# Divider
st.markdown("---")
st.header("📈 Upload and Analyze MALT CSV Log")

uploaded_file = st.file_uploader("Upload a MALT CSV log file", type=["csv"])

if uploaded_file:
    try:
        # Read using correct delimiter and header
        df = pd.read_csv(uploaded_file, header=None)

        # Assign columns based on your format
        df.columns = [
            "Year", "Month", "Day", "Hour", "Minute", "Second",
            "PartID", "MALT_ID", "Test_Program", "Result_Code",
            "Test_Pressure", "Diff_Pressure", "Leak_Rate", "Result_Text"
        ]

        # Combine date and time into one datetime column
        df["Timestamp"] = pd.to_datetime(df[["Year", "Month", "Day", "Hour", "Minute", "Second"]])

        # Preview
        st.subheader("Log Preview")
        st.dataframe(df.head())

        # Plot Test Pressure and Diff Pressure
        st.subheader("📊 Pressure vs Time")

        fig, ax = plt.subplots()
        ax.plot(df["Timestamp"], df["Test_Pressure"], label="Test Pressure (mbar)")
        ax.plot(df["Timestamp"], df["Diff_Pressure"], label="Diff Pressure (Pa or mbar)")
        ax.set_xlabel("Time")
        ax.set_ylabel("Pressure")
        ax.set_title("MALT Pressure Over Time")
        ax.legend()
        st.pyplot(fig)

        # Show result summary
        st.subheader("✅ Result Breakdown")
        result_counts = df["Result_Text"].value_counts()
        st.bar_chart(result_counts)

    except Exception as e:
        st.error(f"Error reading file: {e}")