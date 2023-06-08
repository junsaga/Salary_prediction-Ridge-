import streamlit as st
import numpy as np
import joblib 
import sklearn 
import mglearn

def run_app_ml():
    st.subheader('연봉 금액 예측')

    # 성별, 나이, 연봉, 카드빚, 자산을
    # 유저한테 입력받는다
    gender = st.radio('성별 선택', ['남자', '여자'])
    if gender == '여자':
        gender = 0
    else:
        gender = 1

    EducationLevel = st.radio("학력 선택", ['고졸', '학사', '석사', '박사'])
    if EducationLevel == '고졸':
        EducationLevel = 2
    elif EducationLevel == '학사':
        EducationLevel = 0 or 1
    elif EducationLevel == '석사':
        EducationLevel = 3 or 4
    elif EducationLevel == '박사':
        EducationLevel == 5

    YearsofExperience = st.number_input('Years of Experience', 0, 35)
    Age = st.number_input('나이 입력', 18, 100)
    import numpy as np
    from sklearn.preprocessing import PolynomialFeatures
    # 버튼을 누르면 예측한 금액을 표시한다
    if st.button('금액 예측'):
        lr = joblib.load('model/ridge.pkI')

        my_list = np.array([[Age, gender, EducationLevel, YearsofExperience]])

        my_list = np.array(my_list)
        my_list = my_list.reshape(1, -1)
        poly = PolynomialFeatures(degree=2, include_bias=False)
        poly.fit(my_list)
        # train_poly1 = poly.transform(my_list)
        test_poly1 = poly.transform(my_list)

  # Generate polynomial features manually
        poly = PolynomialFeatures(degree=2, include_bias=False)

        y_pred = lr.predict(test_poly1)

        st.write('예측 금액:',y_pred)

run_app_ml()

    