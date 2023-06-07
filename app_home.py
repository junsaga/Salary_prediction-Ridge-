import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_app_home():

    st.subheader('환영합니다~')
    st.text('좋은 서비스로 제공하겠습니다')
    st.text('자동 배포 처리된 앱입니다.')


    st.text('이 앱은 고객 연봉,나이,재직년수 데이터의 대한 내용입니다')
    st.text('데이터 분석도 가능하고, 고객 정보를 넣으면 연봉도 예측합니다')

    img_url = 'https://t1.daumcdn.net/thumb/R720x0.fjpg/?fname=http://t1.daumcdn.net/brunch/service/user/7XWZ/image/hijq_BqJkTtFvFIdyCXOkCa6E1A.jpg'
    st.image(img_url)