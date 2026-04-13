import streamlit as st

from backend import TemperatureConverter 
st.title("🌡️ Temperature Converter")
choice = st.selectbox("Select an option",['None', 'Celsius -> Fahrenheit', 'Fahrenheit -> Celsius'])
temp = st.number_input("Enter temprature")


temp = TempratureConverter(temp)

if st.button("Convert"):
    if choice == 'None':
        st.warning("Please select a conversion type!")
    else:
        if choice == 'Celsius -> Fahrenheit':
            result = temp.celsius_to_fahrenheit()
        else:
            result = temp.fahrenheit_to_celsius()
    
        st.success(f"🌡️Result: {result:.2f}º")
