import streamlit as st
from streamlit.components.v1 import components

# Code de calcul
def simulate_investment(init_invest, alpha, nb_years, add_year, add_month):
    invest = init_invest
    total = init_invest
    evolution = [init_invest]
    invested = [init_invest]

    for i in range(nb_years):
        new = 0
        new += 12 * add_month
        new += add_year

        invest += new
        invested.append(invest)

        total += new
        total *= (1 + alpha)
        evolution.append(total)

    return invested, evolution

# Interface utilisateur
st.title("Simulateur d'Investissement")

# Choix de la langue
language = st.radio("Choisissez la langue / Choose language:", ("Français", "English"))

# Traduction
if language == "Français":
    st.write("Simulation d'évolution d'investissement sur N années.")
    st.write("Entrez les paramètres ci-dessous :")
    st.write("Investissement initial :")
    init_invest = st.number_input("Montant initial :", min_value=0.0, value=1000.0)
    st.write("Taux de croissance annuelle :")
    alpha = st.number_input("Taux de croissance (en décimal) :", min_value=0.0, value=0.03)
    st.write("Nombre d'années :")
    nb_years = st.number_input("Nombre d'années :", min_value=1, value=100)
    st.write("Contribution annuelle :")
    add_year = st.number_input("Contribution annuelle :", min_value=0.0, value=100.0)
    st.write("Contribution mensuelle :")
    add_month = st.number_input("Contribution mensuelle :", min_value=0.0, value=0.0)

    # Calcul et affichage des résultats
    invested, evolution = simulate_investment(init_invest, alpha, nb_years, add_year, add_month)
    st.line_chart({"Investi": invested, "Valeur totale": evolution})

elif language == "English":
    st.write("Simulation of investment evolution over N years.")
    st.write("Enter the parameters below:")
    st.write("Initial investment:")
    init_invest = st.number_input("Initial amount:", min_value=0.0, value=1000.0)
    st.write("Annual growth rate:")
    alpha = st.number_input("Growth rate (in decimal):", min_value=0.0, value=0.03)
    st.write("Number of years:")
    nb_years = st.number_input("Number of years:", min_value=1, value=100)
    st.write("Annual contribution:")
    add_year = st.number_input("Annual contribution:", min_value=0.0, value=100.0)
    st.write("Monthly contribution:")
    add_month = st.number_input("Monthly contribution:", min_value=0.0, value=0.0)

    # Calculation and display of results
    invested, evolution = simulate_investment(init_invest, alpha, nb_years, add_year, add_month)
    st.line_chart({"Invested": invested, "Total Value": evolution})
