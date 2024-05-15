import pickle
import pandas as pd
import streamlit as st


st.set_page_config(page_title= "Predição", page_icon= "/home/faust/Projetos/DNC/Mes-06/str_mlops/img/stethoscope.png",)
st.sidebar.header('Predição do Arquivo')
st.title('Predição do Seguro')

st.markdown("Prevendo o gasto com o seguro de saúde com base em um arquivo csv:")

# -- Model -- #

with open('./models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

data = st.file_uploader('Carregue seu arquivo')
if data:
    df_input = pd.read_csv(data)
    insurance_prediction = model.predict(df_input)
    df_output = df_input.assign(prediction=insurance_prediction)

    st.markdown('Predição do custo do seguro:')
    st.write(df_output)
    st.download_button(label='Download CSV', data=df_output.to_csv(index=False), mime='text/csv', file_name='predicted_insurance.csv')