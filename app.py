import streamlit as st
import pandas as pd

st.header("Welcome to the page!")
st.subheader("A page using streamlit:sunglasses:")
st.text("stream used to build this app in a very easy way.")

df= pd.read_csv(r"C:\Users\Admin\Desktop\Yakub_ML\Parkinsondata.csv")

st.dataframe(df)