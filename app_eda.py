import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_app_eda():
    st.subheader('데이터 분석')

    df = pd.read_csv('data/Car_Purchasing_Data (1).csv',encoding='ISO-8859-1')
    print(df)

    if st.checkbox('데이터 프레임 보기'):
        st.dataframe(df)
    
    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())

    st.subheader('최대 / 최소 데이터 확인하기')

    column=st.selectbox('컬럼을 선택하세요.',df.columns[3 : ])

    st.text('최대 데이터')
    st.dataframe(df.loc[df[column] ==df[column].max(),])
    st.text('최소 데이터')
    st.dataframe(df.loc[df[column] ==df[column].min(),])
    st.subheader('컬럼 별 히스토그램')

    column = st.selectbox('히스토그램 확인할 컬럼을 선택하세요.',df.columns[ 3: ])
    bins=st.number_input('빈의 갯수를 입력하세요.',10,30,20)

    fig = plt.figure()
    df[column].hist(bins=bins)

    plt.title(column + 'Histogram')
    plt.xlabel(column)
    plt.ylabel('count')

    st.subheader("상관 관계 분석")
    column_list = st.multiselect('상관분석 하고 싶은 컬럼을 선택하세요.',df.columns[3:])

    if len(column_list) >= 2:
        fig2 =plt.figure()
        sns.heatmap(data=df.corr(numeric_only=True),
                annot= True,vmin=-1,vmax=1,
                cmap='coolwarm',fmt='.2f',linewidths = 0.5)
        st.pyplot(fig2)

    print(column_list)
    df[column_list].corr()
    st.pyplot(fig)