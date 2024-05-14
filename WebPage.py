#-*- coding: utf-8 -*-
from datetime import datetime

import numpy as np
import sklearn
import pandas as pd
import streamlit as st
import pickle
st.set_page_config(
    page_title="GaryChern",
    page_icon="📊",
    initial_sidebar_state="collapsed",
    layout="wide")# 设置页面配置为全屏显示

# 创建两列
# 创建两列，指定宽度比例
col1, col2 = st.columns([1, 1])

# 在第一列中放置内容
with col1:
    #st.header('左侧列')
    #st.write('这是左侧列的内容。')
    st.title("Risk Prediction Platform")

    st.subheader("Demographic Data")
    selected_Age = st.number_input('Your Age Is:', min_value=1, max_value=100, step=1)
    # 根据年龄值分类
    if selected_Age < 30:
        selected_Age_number = 3
    elif selected_Age >= 30 and selected_Age < 40:
        selected_Age_number = 3
    elif selected_Age >= 40 and selected_Age < 50:
        selected_Age_number = 4
    elif selected_Age >= 50 and selected_Age < 60:
        selected_Age_number = 5
    elif selected_Age >= 60 and selected_Age < 70:
        selected_Age_number = 6
    elif selected_Age >= 70 and selected_Age < 80:
        selected_Age_number = 7
    elif selected_Age >= 80 and selected_Age < 90:
        selected_Age_number = 8
    else:
        selected_Age_number = 9

    selected_Gender = st.selectbox('Your Gender Is:', ['Male', 'Female'])
    if selected_Gender == 'Male':
        selected_Gender_number = 1
    else:
        selected_Gender_number = 2
    # 设置数字输入框的最小值为0.0，最大值为10.0，步进值为0.1
    selected_BMI = st.number_input('Your BMI Is:', min_value=0.0, max_value=50.0, step=0.1)

    st.subheader("Previous Medical History Data")
    options = ['YES', 'NO']
    selected_HT = st.radio('Do you have a history of hypertension?', options)
    if selected_HT == 'YES':
        selected_HT_number = 1
    else:
        selected_HT_number = 0
    selected_PreviousStroke_TIA = st.radio('Do you have a history of PreviousStroke_TIA?', options)
    if selected_PreviousStroke_TIA == 'YES':
        selected_PreviousStroke_TIA_number = 1
    else:
        selected_PreviousStroke_TIA_number = 0
    selected_DM = st.radio('Do you have a history of Diabetes Mellitus?', options)
    if selected_DM == 'YES':
        selected_DM_number = 1
    else:
        selected_DM_number = 0
    selected_Hyperlipidemia = st.radio('Do you have a history of Hyperlipidemia?', options)
    if selected_Hyperlipidemia == 'YES':
        selected_Hyperlipidemia_number = 1
    else:
        selected_Hyperlipidemia_number = 0
    selected_Af = st.radio('Do you have a history of Atrial Fibrillation?', options)
    if selected_Af == 'YES':
        selected_Af_number = 1
    else:
        selected_Af_number = 0
    selected_CHD = st.radio('Do you have a history of Coronary Heart Disease?', options)
    if selected_CHD == 'YES':
        selected_CHD_number = 1
    else:
        selected_CHD_number = 0
    selected_Smoking = st.radio('Do you have a history of Smoking?', options)
    if selected_Smoking == 'YES':
        selected_Smoking_number = 1
    else:
        selected_Smoking_number = 0

    st.subheader("Hematological Examination Data")
    selected_WBC = st.number_input('WBC(Body Mass Index)-(×10^9/L)', min_value=0.0, max_value=40.0, step=0.1)
    selected_RBC = st.slider('RBC(Red Blood Cell Count)-(×10^12/L)', min_value=0.0, max_value=10.0, step=0.1)
    selected_Hb = st.slider('Hb(Hemoglobin)-(g/dL)', min_value=0.0, max_value=20.0, step=0.1)
    selected_PLT = st.slider('PLT(Platelet Count)-(×10^9/L)', min_value=0.0, max_value=1000.0, step=1.0)
    selected_FIB = st.slider('FIB(Fibrinogen)-(mg/dL)', min_value=0.0, max_value=1000.0, step=1.0)




    # 在第二列中放置内容
with col2:
    #st.header('右侧列')
    #st.write('这是右侧列的内容。')
    # image ='./Images/Stroke_infographic_risk_of_stroke_QBI.png'
    # st.image(image, caption=None, use_column_width=True, output_format='auto')
    st.subheader("Inflammation Markers")
    selected_CRP = st.slider('CRP(C-Reactive Protein)-(mg/dL)', min_value=0.0, max_value=30.0, step=0.1)
    selected_ESR = st.slider('ESR(Erythrocyte Sedimentation Rate)-(mm/h)', min_value=0.0, max_value=150.0, step=0.1)

    st.subheader("Renal and Liver Function Markers")
    selected_BUN = st.number_input('BUN(Blood Urea Nitrogen)-(mg/dL)', min_value=0.0, max_value=100.0, step=0.1)
    selected_Scr = st.number_input('Scr(Serum Creatinine)-(mg/dL)', min_value=0.0, max_value=20.0, step=0.1)
    selected_AST = st.number_input('ALT(Aspartate Aminotransferase)-(U/L)', min_value=0.0, max_value=300.0, step=1)
    selected_ALT = st.number_input('AST(Alanine Aminotransferase)-(U/L)', min_value=0.0, max_value=200.0, step=1)
    selected_Albumin = st.number_input('Albumin-(g/dL)', min_value=0.0, max_value=10.0, step=0.1)
    selected_TotolProtein = st.number_input('Total protein-(g/dL)', min_value=0.0, max_value=10.0, step=0.1)

    st.subheader("Blood Lipid and Blood Glucose Indicators")
    selected_TC = st.slider('TC(Total Cholesterol)-(mg/dL)', min_value=0.0, max_value=500.0, step=0.1)
    selected_TG = st.slider('TG(Triglyceride)-(mg/dL)', min_value=0.0, max_value=700.0, step=0.1)
    selected_HDL_C = st.slider('HDL-C(High-Density Lipoprotein Cholesterol)-(mg/dL)', min_value=0.0, max_value=200.0, step=0.1)
    selected_LDL_C = st.slider('LDL-C(Low-Density Lipoprotein Cholesterol)-(mg/dL)', min_value=0.0, max_value=400.0, step=0.1)
    selected_FBG = st.slider('FBG(Fasting Plasma Glucose)-(mg/dL)', min_value=0.0, max_value=450.0, step=0.1)
    #selected_HbA1c = st.number_input('Hemoglobin A1c', min_value=0.0, max_value=50.0, step=0.1)
    selected_HbA1c = st.slider('HbA1c(Hemoglobin A1c)-(%)', 0.0, 20.0, value=None, step=0.1)

    st.subheader("StrokeEtiology")
    options = ['LAA', 'SAO', 'CE', 'Other determined', 'Undetermined']
    selected_StrokeEtiology = st.selectbox('StrokeEtiology', options)
    if selected_StrokeEtiology == 'LAA':
        selected_StrokeEtiology_number = 1
    elif selected_StrokeEtiology == 'SAO':
        selected_StrokeEtiology_number = 2
    elif selected_StrokeEtiology == 'CE':
        selected_StrokeEtiology_number = 3
    elif selected_StrokeEtiology == 'Other determined':
        selected_StrokeEtiology_number = 4
    else:
        selected_StrokeEtiology_number = 5

    submit_button = st.button("Submit")  # 添加提交按钮

if submit_button:
    Results = None
    st.subheader("")


    # 创建一个包含获取的数据的字典
    data = {
        'HT': [selected_HT_number],
        'Age': [selected_Age_number],
        'Gender': [selected_Gender_number],
        'BMI': [selected_BMI],
        'PreviousStroke_TIA': [selected_PreviousStroke_TIA_number],
        'DM': [selected_DM_number],
        'Hyperlipidemia': [selected_Hyperlipidemia_number],
        'Af': [selected_Af_number],
        'CHD': [selected_CHD_number],
        'Smoking': [selected_Smoking_number],
        'WBC': [selected_WBC],
        'RBC': [selected_RBC],
        'Hb': [selected_Hb],
        'PLT': [selected_PLT],
        'FIB': [selected_FIB],
        'CRP': [selected_CRP],
        'ESR': [selected_ESR],
        'BUN': [selected_BUN],
        'Scr': [selected_Scr],
        'AST': [selected_AST],
        'ALT': [selected_ALT],
        'Albumin': [selected_Albumin],
        'TotolProtein': [selected_TotolProtein],
        'TC': [selected_TC],
        'TG': [selected_TG],
        'HDL_C': [selected_HDL_C],
        'LDL_C': [selected_LDL_C],
        'FBG': [selected_FBG],
        'HbA1c': [selected_HbA1c],
        'StrokeEtiology': [selected_StrokeEtiology_number],
    }

    # df_data = pd.DataFrame(data)
    # # 显示 DataFrame
    # st.write(df_data)
    #引入机器学习模型进行预测
    # 加载模型
    with open('voting_classifier.pkl', 'rb') as f:
        model = pickle.load(f)
    # 提取特征值
    features = [[selected_HT_number, selected_Age_number, selected_Gender_number, selected_BMI, selected_PreviousStroke_TIA_number, selected_DM_number, selected_Hyperlipidemia_number, selected_Af_number, selected_CHD_number, selected_Smoking_number, selected_WBC, selected_RBC, selected_Hb, selected_PLT, selected_FIB, selected_CRP, selected_ESR, selected_BUN, selected_Scr, selected_AST, selected_ALT, selected_Albumin, selected_TotolProtein, selected_TC, selected_TG, selected_HDL_C, selected_LDL_C, selected_FBG, selected_HbA1c, selected_StrokeEtiology_number]]
    prediction = model.predict_proba(features)

    # 提取出第一个类别的概率值
    probability_FavorableOutcomes = prediction[0][0]
    # 提取出第二个类别的概率值
    probability_UnfavorableOutcomes = prediction[0][1]
    if probability_UnfavorableOutcomes >= 0.435548:
        temp = 0.5+((probability_UnfavorableOutcomes - 0.435548)*(1-0.435548)/0.5)
        st.subheader("Results Of Stroke Prognosis is UnfavorableOutcomes!"+"And this  probability has reached:"+str("{:.3f}".format(temp)))
        # st.subheader("Results Of Stroke Prognosis is UnfavorableOutcomes!"+"And this risk probability has reached:"+str("{:.3f}".format(probability_UnfavorableOutcomes)))
    else:
        temp = 1 - ((0.435548 - probability_UnfavorableOutcomes) * ((1 - 0.435548) / 0.5))
        st.subheader("Results Of Stroke Prognosis is FavorableOutcomes!"+"And this probability has reached:"+str("{:.3f}".format(temp)))

    # 将字典转换为 DataFrame
    df = pd.DataFrame(data)
    # 显示 DataFrame
    st.write(df)





