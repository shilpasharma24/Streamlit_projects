
import streamlit as st
import requests

st.title("Weather API Demo")

# Read API key from secrets
API_KEY = st.secrets.get("API_KEY", "demo_key")

# Enter city
city = st.text_input("Enter city", "Chennai")

if st.button("Get Weather"):

    # Simulated weather response
    resp = {
        "city": city,
        "temperature": 30,
        "condition": "Sunny",
        "humidity": 65
    }

    # Display JSON data
    st.json(resp)

    # Display weather metrics
    c1, c2, c3 = st.columns(3)

    c1.metric("Temperature", f"{resp['temperature']} °C")
    c2.metric("Condition", resp["condition"])
    c3.metric("Humidity", f"{resp['humidity']}%")

st.markdown("---")

st.subheader("HTTP Methods")

st.markdown("""
- **GET** - Retrieve data
- **POST** - Send data
- **PUT** - Update data
- **DELETE** - Delete data
""")
