import streamlit as st
from PIL import Image

st.title('fumioアプリ')
st.caption('これは文夫の動画用テストアプリです')

image = Image.open('./data/6992.jpg')
st.image(image, width=300)