import streamlit as st
import pandas as pd

st.title("🥨🥨WedSite Developing using Python🥨🥨")
st.header("🥪WedSite Developing using Python🥪")

st.image('./img/์NiceMewing.jfif')
st.subheader("Nice Lnwza007")

dt = pd.read_csv('./data/iris.csv')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))