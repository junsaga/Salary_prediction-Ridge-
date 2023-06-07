import streamlit as st
import numpy as np
import joblib 
import sklearn 
def run_app_ml():
    st.subheader('연봉 금액 예측')
    

    # 성별, 나이, 연봉,카드빚 , 자산을
    # 유저한테 입력받는다
    gender =st.radio('성별 선택',['남자','여자'])
    if gender =='여자':
        gender =0
    else:
        gender =1

    EducationLevel = st.radio("학력 선택",['고졸','학사','석사','박사'])
    if EducationLevel =='고졸':
        EducationLevel =2
    elif EducationLevel =='학사':
        EducationLevel =0 or 1
    elif EducationLevel =='석사':
        EducationLevel =3 or 4
    elif EducationLevel =='박사':
        EducationLevel ==5
    
    YE = st.number_input('Years of Experience',0,35)
    age = st.number_input('나이 입력',18,100)   

    # 버튼을 누르면 예측한 금액을 표시한다

    if st.button('금액 예측'):

        new_data = np.array([gender,age,EducationLevel,YE,age])

        new_data = new_data.reshape(1,5)

        lr=joblib.load('model/Ridge.pkI')

        y_pred=lr.predict(new_data)

        print(round(y_pred[0]))

        price = round(y_pred[0])

    # 버튼을 누르면 예측한 금액을 표시한다

    