import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


st.set_page_config(page_title='Breast Cancer Wisconsin Diagnosis',
                   layout='wide', 
                   page_icon='🩺')

diagnosis_model = pickle.load(open(r"..\Breast Cancer Wisconsin Diagnosis\diagnosis_model.sav",'rb'))


st.title('Breast Cancer Wisconsin Diagnosis 🧑‍⚕️')
col1,col2,col3,col4,col5=st.columns(5)
with col1:
    radius_mean=st.text_input('Average radius')
with col2:
    perimeter_mean=st.text_input('Average perimeter')
with col3:
    area_mean=st.text_input('Average area')
with col4:
    concavity_mean=st.text_input('Average concavity')
with col5:
    concave_points_mean=st.text_input('Average number of concave points')
with col1:
    radius_worst=st.text_input('Worst-case radius')
with col2:
    perimeter_worst=st.text_input('Worst-case perimeter')
with col3:
    area_worst=st.text_input('Worst-case area')
with col4:
    concavity_worst=st.text_input('Worst-case concavity')
with col5:
    concave_points_worst=st.text_input('Worst-case number of concave points')

canc_diagnosis=''

if st.button('Diagnosis Result'):
    user_input=[[radius_mean,perimeter_mean,area_mean,concavity_mean,concave_points_mean,radius_worst,
                perimeter_worst,area_worst,concavity_worst,concave_points_worst]]
    user_input = scaler.transform(user_input)
    user_input=user_input.reshape(-1)
    user_input=[float(x) for x in user_input]
    canc_prediction=diagnosis_model.predict([user_input])
    if canc_prediction[0]==1:
        canc_diagnosis='The person is Malignant'
    else:
        canc_diagnosis='The person is Benign'
st.success(canc_diagnosis)
