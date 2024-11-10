import streamlit as st
from datetime import datetime, timedelta

# Set page config
st.set_page_config(page_title="Lab Sample Timer", page_icon="⏰", layout="centered")

# Define allowed duration and buffer time
allowed_duration = timedelta(hours=8, minutes=20)
buffer_time = timedelta(minutes=30)

# Title and instructions
st.title("Lab Sample Timer")
st.write("This tool helps check if a sample is 'OK', 'Old on Arrival', or 'Old'.")

# Input bucket time
bucket_time_str = st.text_input("Enter Bucket Time (HH:MM)", placeholder="e.g., 19:00")

# Check button
if bucket_time_str:
    try:
        bucket_time = datetime.strptime(bucket_time_str, "%H:%M")
        current_time = datetime.now()
        
        # Calculate status
        def check_status(sample_time):
            sample_datetime = datetime.combine(datetime.today(), sample_time.time())
            elapsed_time = sample_datetime - bucket_time
            
            if elapsed_time <= allowed_duration:
                return "OK"
            elif elapsed_time <= allowed_duration + buffer_time:
                return "Old on Arrival"
            else:
                return "Old"

        # Input sample time
        sample_time_str = st.text_input("Enter Sample Time (HH:MM)", placeholder="e.g., 21:30")
        if sample_time_str:
            sample_time = datetime.strptime(sample_time_str, "%H:%M")
            status = check_status(sample_time)
            st.write(f"Sample Status: **{status}**")

        # Display countdown to "old" time
        time_left = bucket_time + allowed_duration - current_time
        if time_left.total_seconds() > 0:
            st.write(f"Time left until old: **{time_left}**")
        else:
            st.write("Samples are now **OLD**")
    except ValueError:
        st.error("Please enter the time in HH:MM format.")
