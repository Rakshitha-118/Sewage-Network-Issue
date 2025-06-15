import streamlit as st
import random
import datetime

# Simulated live data
tank_level = random.randint(60, 95)
inflow = random.randint(200, 350)
outflow = inflow - random.randint(0, 20)
pump_status = random.choice(['ON', 'OFF'])
power_status = random.choice(['Normal', 'Failure'])

# Header
st.title("Surathkal Sewerage SCADA-lite Dashboard")
st.write("🕒", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Live status panel
st.subheader("Live Monitoring Status")
st.metric("Pump Status", pump_status)
st.metric("Tank Level (%)", tank_level)
st.metric("Inflow Rate (L/min)", inflow)
st.metric("Outflow Rate (L/min)", outflow)
st.metric("Power Status", power_status)

# Alerts
st.subheader("⚠ Alerts")
if tank_level > 90:
    st.error(f"Overflow Alert: Tank level is at {tank_level}%!")
if pump_status == "OFF":
    st.warning("Pump is OFF. Check for inactivity.")
if power_status == "Failure":
    st.error("Power Failure Detected at Site!")