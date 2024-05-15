import streamlit as st

st.set_page_config(
    page_title= "Insurence Prediction",
    page_icon= "/home/faust/Projetos/DNC/Mes-06/str_mlops/img/stethoscope.png",
)

st.sidebar.header('Project Discription')

st.write('# Bem vindo ao Aplicativo de Predição de Seguros de Saúde')
st.write('\n\n')

st.image('/home/faust/Projetos/DNC/Mes-06/str_mlops/img/health_insurance_img.jpg')
st.write('\n\n')

st.markdown(
    """
    Predições Seguros de saúde são fundamentais para o setor da saúde, uma vez que elas ajudam a determinar os custos associados a esse produto.
    Analisando fatores demográficos, históricos médicos, e estilo de vida podemos criar predições para alocar recursos de forma mais eficiente.
    De maneira geral, essa ferramente de predição é valiosa tanto para seguradouras como para consumidores.

    Esse aplicativo mira fazer uma previsão dos custos com o seguro de saude através de variáveis como:
    - idade
    - BMI
    - Número de filhos
    """
)

st.success('Por favor **siga para a próxima página** para as previsões')