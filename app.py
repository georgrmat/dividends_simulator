import streamlit as st
#import matplotlib.pyplot as plt
import numpy as np

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
language = st.sidebar.radio("Language / Langue", ("English", "Français"))

# Traduction
if language == "Français":
    st.write("Simulation d'évolution d'investissement sur N années")
    st.sidebar.write("Paramètres")
    init_invest = st.sidebar.number_input("Investissement initial", min_value=0.0, value=1000.0)
    alpha = st.sidebar.number_input("Taux de croissance annuelle", min_value=0.0, value=0.03)
    nb_years = st.sidebar.slider("Nombre d'années", min_value=1, max_value=100, value=50)
    add_year = st.sidebar.number_input("Contribution annuelle", min_value=0.0, value=100.0)
    add_month = st.sidebar.number_input("Contribution mensuelle", min_value=0.0, value=0.0)

    # Calcul et affichage des résultats
    invested, evolution = simulate_investment(init_invest, alpha, nb_years, add_year, add_month)
    st.line_chart({"Investi": invested, "Valeur totale": evolution})

elif language == "English":
    st.write("Simulation of investment evolution over N years")
    st.sidebar.write("Parameters:")
    init_invest = st.sidebar.number_input("Initial investment", min_value=0.0, value=1000.0)
    alpha = st.sidebar.number_input("Annual growth rate", min_value=0.0, value=0.03)
    nb_years = st.sidebar.slider("Number of years", min_value=1, max_value=100, value=50)
    add_year = st.sidebar.number_input("Annual contribution", min_value=0.0, value=100.0)
    add_month = st.sidebar.number_input("Monthly contribution", min_value=0.0, value=0.0)

    # Calculation and display of results
    invested, evolution = simulate_investment(init_invest, alpha, nb_years, add_year, add_month)
    st.line_chart({"Invested": invested, "Total Value": evolution})
