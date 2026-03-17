import streamlit as st
from PIL import Image ,ImageFilter

st.title("Image Filter")
img = st.file_uploader("Upload an image",type = ["jpg","png","jpeg"])

if img:

    img = Image.open(img)
    option = st.selectbox("Select Filter",["ORIGINAL","GRAYSCALE","BLUR","CONTOUR"])

    if option == "GRAYSCALE":
        img = img.convert("L")

    elif option == "CONTOUR":
        img = img.filter(ImageFilter.CONTOUR)

    elif option == "BLUR":
        img = img.filter(ImageFilter.BLUR)

        
    st.image(img)
    

