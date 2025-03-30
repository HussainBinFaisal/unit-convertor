import streamlit as st

#length
def convert_length(value, from_unit, to_unit):
    length_units = {"meters": 1, "kilometers": 0.001, "centimeters": 100, "millimeters": 1000, "miles": 0.000621371, "yards": 1.09361, "feet": 3.28084, "inches": 39.3701}
    return value * length_units[to_unit] / length_units[from_unit]

#weight

def convert_weight(value, from_unit, to_unit):
    weight_units = {"kilograms": 1, "grams": 1000, "milligrams": 1e6, "pounds": 2.20462, "ounces": 35.274}
  
    return value * weight_units[to_unit] / weight_units[from_unit]
#temp
def convert_temperature(value, from_unit, to_unit):
    conversions = {
        ("Celsius", "Fahrenheit"): (value * 9/5) + 32,
        ("Fahrenheit", "Celsius"): (value - 32) * 5/9,
        ("Celsius", "Kelvin"): value + 273.15,
        ("Kelvin", "Celsius"): value - 273.15,
        ("Fahrenheit", "Kelvin"): (value - 32) * 5/9 + 273.15,
        ("Kelvin", "Fahrenheit"): (value - 273.15) * 9/5 + 32,
    }
    return conversions.get((from_unit, to_unit), value)

#title
st.title("🔥 Simple Unit Converter")

category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

value = st.number_input("Enter Value", min_value=0.0, format="%.6f") #decimal Code

if category == "Length":
    from_unit = st.selectbox("From Unit", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
    to_unit = st.selectbox("To Unit", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
    result = convert_length(value, from_unit, to_unit)



elif category == "Weight":
    from_unit = st.selectbox("From Unit", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
    to_unit = st.selectbox("To Unit", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
    result = convert_weight(value, from_unit, to_unit)





elif category == "Temperature":
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    result = convert_temperature(value, from_unit, to_unit)


if st.button("Convert 🔄"):
    st.success(f"Converted Value: {result:.6f} {to_unit}")
