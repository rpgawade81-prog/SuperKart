
import streamlit as st
import requests
import os

# Get backend URL from environment variable or default to localhost
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:5000")

st.title("Product Sales Prediction App") #Complete the code to define the title of the app.

# Input fields for product and store data
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area = (
    st.number_input("Product Allocated Area", min_value=0.0, value=0.1)
) #Complete the code to define the UI element for Product_Allocated_Area
Product_MRP = st.number_input("Product MRP", min_value=0.0, value=100.0) #Complete the code to define the UI element for Product_MRP
Store_Size = st.selectbox(
    "Store Size", ["Small", "Medium", "High"]
) #Complete the code to define the UI element for Store_Size
Store_Location_City_Type = st.selectbox(
    "Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"]
) #Complete the code to define the UI element for Store_Location_City_Type
Store_Type = st.selectbox(
    "Store Type", ["Supermarket Type1", "Supermarket Type2", "Grocery Store"]
) #Complete the code to define the UI element for Store_Type
Product_Id_char = st.text_input(
    "Product ID Character", value="FD"
) #Complete the code to define the UI element for Product_Id_char
Store_Age_Years = st.number_input(
    "Store Age Years", min_value=0, value=10
) #Complete the code to define the UI element for Store_Age_Years
Product_Type_Category = st.selectbox(
    "Product Type Category", ["Perishables", "Non Perishables"]
) #Complete the code to define the UI element for Product_Type_Category

product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_char": Product_Id_char,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category
}

if st.button("Predict", type='primary'):
    try:
        response = requests.post(f"{BACKEND_URL}/predict", json=product_data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            predicted_sales = result.get("Prediction", result.get("prediction"))
            st.success(f"Predicted Product Store Sales Total: ₹{float(predicted_sales):.2f}")
        else:
            st.error(f"Error in API request: {response.text}")
    except requests.exceptions.ConnectionError:
        st.error(f"Cannot connect to backend at {BACKEND_URL}. Please check if the API is running.")
    except requests.exceptions.Timeout:
        st.error("Request to backend timed out. Please try again.")
    except Exception as e:
        st.error(f"Error: {str(e)}")
