import streamlit as st
from PIL import Image
st.title('アプリ名')
st.caption('テストです')

image = Image.open('./data/01.png')
st.image(image, width=300)
