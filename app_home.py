import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_app_home():

    st.subheader('안녕하세요')

    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다')
    st.text('데이터 분석도 가능하고, 고객 정보를 넣으면 구매 차량 가격도 예측합니다')

    img_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvg-HluWp-n9HaTl74JiqZPgfI4o_elyMpCQ&usqp=CAU'
    st.image(img_url)