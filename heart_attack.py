import pandas as pd
import numpy as np
import streamlit as st
import joblib

model = joblib.load('tipis\death_heart.pkl')
all_columns = ['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 'ejection_fraction', 'high_blood_pressure',
               'platelets', 'serum_creatinine', 'serum_sodium', 'sex', 'smoking', 'time']

st.title('Прогноз смерти от сердечного приступа')

age = st.number_input('Ваш возраст', min_value=20, max_value=100, value=20, step=1)
anaemia = st.number_input('Есть ли у Вас анемия? (Нет/0, Да/1)', min_value=0, max_value=1, value=0, step=1)
creatinine_phosphokinase = st.number_input('Ваш уровень креатинкиназа (мкг/л)', min_value=20, max_value=8000, value=20, step=1)
diabetes = st.number_input('Есть ли у Вас диабет? (Нет/0, Да/1)', min_value=0, max_value=1, value=0, step=1)
ejection_fraction = st.number_input('Укажите фракцию выброса (в процентах)', min_value=14, max_value=90, value=14, step=1)
high_blood_pressure = st.number_input('Есть ли у Вас гипертония? (Нет/0, Да/1)', min_value=0, max_value=1, value=0, step=1)
platelets = st.number_input('Количество тромбоцитов в крови (килотромбоцитов/мл)', min_value=20000, max_value=850000, value=20000, step=1000)
serum_creatinine = st.number_input('Уровень креатинина (мг/дл)', min_value=0.0, max_value=10.0, value=0.0, step=0.01)
serum_sodium = st.number_input('Уровень натрия в крови (мЭкв/л)', min_value=110, max_value=150, value=110, step=1)
sex = st.number_input('Ваш пол (М/0, Ж/1)', min_value=0, max_value=1, value=0, step=1)
smoking = st.number_input('Курите? (Нет/0, Да/1)', min_value=0, max_value=1, value=0, step=1)
time = st.number_input('Период наблюдения (сутки)', min_value=3, max_value=365, value=3, step=1)

input_data = {'age': age, 
              'anaemia': anaemia, 
              'creatinine_phosphokinase': creatinine_phosphokinase, 
              'diabetes': diabetes,
              'ejection_fraction': ejection_fraction, 
              'high_blood_pressure': high_blood_pressure, 
              'platelets': platelets,
              'serum_creatinine': serum_creatinine, 
              'serum_sodium': serum_sodium, 
              'sex': sex, 
              'smoking': smoking, 
              'time': time}

input_df = pd.DataFrame([input_data], columns=all_columns).fillna(0)

if st.button('Предсказать смерть'):
    prediction = model.predict(input_df)
    if prediction[0] == 1:
        death = 'С шансом в 83% Вы умрете от сердечного приступа. Я Вам не завидую. Советую начать лечиться.'
    else:
        death = 'С шансом в 83% Вы не умрете из-за сердца. Но это не означает, что вы в принципе не умрете.'

    st.success(f'Умрете ли Вы в течение периода наблюдения {int(time)} суток? {death}')