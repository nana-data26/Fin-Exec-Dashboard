import streamlit as st
import pandas as pd
import numpy as np

#Para rodar a aplicação: streamlit run app.py
#Para cancelar a aplicação: Ctrl + C

#----------------------------------------------------------------------------------#

st.title("EXECUTIVE FINANCIAL DASHBOARD")

#----------------------------------------------------------------------------------#
#Cache


@st.cache_data
def load_data():
    return pd.read_csv("ecommerce_sales_data.csv" , sep=",", encoding='utf-8-sig')

sales_data = load_data()

#----------------------------------------------------------------------------------#

#Session State Control

#Reseta contador quando a categoria mudar

def on_change():
    st.session_state.counter = 0

#----------------------------------------------------------------------------------#

#sales_data.dtypes
#Order Date: object
#Product Name: object
#Category: object
#Region: object
#Quantity: int64
#Sales: int64
#Profit: float64

#Altera Coluna Order Date para Datetime
sales_data["Order Date"] = pd.to_datetime(sales_data["Order Date"])

#----------------------------------------------------------------------------------#

# Inicialização

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.selectbox (
    "Category",
    options = sales_data["Category"].unique(),
    key = "category",
    on_change = on_change
)

if st.button("Run"):
    st.session_state.counter += 1

st.write("Categoria: ", st.session_state.category)
st.write("Counter: ", st.session_state.counter)

#----------------------------------------------------------------------------------#

#Teste da Data

st.select_slider (
    "Date",
    options = sales_data["Order Date"].unique(),
    key = "date",
    on_change = on_change
)