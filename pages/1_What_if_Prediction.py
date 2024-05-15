import pickle
import pandas as pd
import streamlit as st

# Page Config
st.set_page_config(
    page_title= "Predição",
    page_icon= "/home/faust/Projetos/DNC/Mes-06/str_mlops/img/stethoscope.png",
)

st.sidebar.header('Predição')
st.title('Predição do Seguro')

st.markdown("Prevendo o gasto com o seguro de saúde com base nos seguintes parâmetros:")

# -- Parameters -- #

age= st.number_input(label='Age', value=18, min_value=18, max_value=120)
bmi= st.number_input(label='BMI', value=30.0)
children = st.slider(label='Children', min_value=0, max_value=5)
smoker = st.selectbox(label='Smoker', options=['no', 'yes'])

# -- Model -- #

with open('../models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Função para fazer uma predição
def prediction():
    df_input = pd.DataFrame([{
        'age': age,
        'bmi': bmi,
        'children': children,
        'smoker': smoker
    }])
    prediction = model.predict(df_input)[0]
    return prediction


# Adicionando um Botão
if st.button('Predict'):
    try:
        insurence = prediction()
        st.success(f'**Prever custo do seguro de saúde:** ${insurence:,.2f}')
    except Exception as error:
        st.error(f"Não foi possível realizar a predição. O error seguinte ocorreu: \n\n{error}")