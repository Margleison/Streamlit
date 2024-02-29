import streamlit as st


with st.sidebar:
    st.title("Calculadora IMC")
    st.write("Indice De Massa Corporal (IMC)")

st.title("Calculadora")

altura = st.number_input(label="Digite a sua altura", min_value= 0.0)

peso = st.number_input(label="Digite o seu peso em kg", min_value= 0.0)


if st.button("Calcular"):
    imc = peso / (altura ** 2)
    imc_ideal = 21.5
    imc_delta = imc - imc_ideal
    st.write(f"O IMC ideal é: {imc_ideal}")

    if imc < 18.5:
        resultado = {
            "IMC" : (f"{imc:.1f}"),
            "Classe": 'Abaixo do peso',
            "Delta": imc_delta
        } 
    elif imc >= 20.8:
        st.write("Essa tal de Beatriz Agnes é perfeita até nisso!!")
        st.write("!!!UMA GRANDE GOSTOSA ESSA MULHER!!!!")
        resultado = {
            "IMC" : (f"{imc :.1f}"),
            "Classe": 'Peso ideal',
            "Delta": imc_ideal
        }
    elif imc >= 18.5 and imc <= 25:
        resultado = {
            "IMC" : (f"{imc :.1f}"),
            "Classe": 'Peso ideal',
            "Delta": imc_ideal
        }
    elif imc > 25 and imc <= 30:
        resultado = {
            "IMC" : (f"{imc :.1f}"),
            "Classe": 'Sobrepeso',
            "Delta": imc_delta
        }
    elif imc > 30 and imc <= 35:
        resultado = {
            "IMC" : (f"{imc :.1f}"),
            "Classe": 'Obesidade',
            "Delta": imc_delta
        }

    elif imc > 35:
        resultado = {
            "IMC" : (f"{imc :.1f}"),
            "Classe": 'Obesidade II',
            "Delta": imc_delta
        }
    else:
        resultado = {
            "IMC" : (f"{imc :.1f}"),
            "Classe": 'Obesidade Morbida',
            "Delta": imc_delta
        }

    st.code(f"O seu IMC é {resultado}")

    col1, col2= st.columns(2)

    
    col1.metric("IMC Calculado", round(imc, 2), resultado["Delta"], delta_color="inverse")
    col2.metric("IMC Classificado", resultado ["Classe"], resultado ["Delta"], delta_color="normal")
    
    st.divider()
    st.text("Fonte")

    st.image("./peso.png")
    st.image("./escala-IMC-logo.webp")