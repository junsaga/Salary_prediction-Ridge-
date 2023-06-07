import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
label_encoder = LabelEncoder()
def run_app_eda():
    st.subheader('데이터 분석')

    df = pd.read_csv('data/Salary_Data.csv')
    print(df)

    if st.checkbox('데이터 프레임 보기'):
        st.dataframe(df)
    
    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())
    
    column = st.selectbox('히스토그램 확인할 컬럼을 선택하세요.',df.columns[ : ])
    bins=st.number_input('빈의 갯수를 입력하세요.',10,30,20)

    # df column Gender 문자값을 숫자값으로 변경
    df['Gender'] = label_encoder.fit_transform(df['Gender'])
    # df column Education Level 문자값을 숫자값으로 변경
    df['Education Level'] = label_encoder.fit_transform(df['Education Level'] )
    fig = plt.figure()
    df[column].hist(bins=bins)

    plt.title(column + 'Histogram')
    plt.xlabel(column)
    plt.ylabel('count')

    st.subheader("상관 관계 분석")
    column_list = st.multiselect('상관분석 하고 싶은 컬럼을 선택하세요.',df.columns[0:])

    if len(column_list) >= 2:
        fig2 =plt.figure()
        sns.heatmap(data=df.corr(numeric_only=True),
                annot= True,vmin=-1,vmax=1,
                cmap='coolwarm',fmt='.2f',linewidths = 0.5)
        st.pyplot(fig2)
    
    
    print(column_list)
    df[column_list].corr()
    st.pyplot(fig)