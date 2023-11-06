import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Used Car App"
)



st.title("Welcome")
st.title("Are you looking to buy or sell a used car?")
st.sidebar.success("Select an option above.")

st.write("This app will help you on making a decision on buying or selling a car.")

st.write("Choose an option on the sidebar.")

#https://www.digitaltrends.com/cars/2020-lamborghini-huracan-evo-review/
image = Image.open('car_picture.png')
st.image(image)