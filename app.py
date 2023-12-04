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
        total *= (1 + alpha/10)
        evolution.append(total)

    return invested, evolution

# Interface utilisateur
# Choix de la langue
language = st.sidebar.radio("Language / Langue", ("English", "Français"))

# Traduction
if language == "Français":
    st.title("Simulateur d'Investissement")
    st.write("Simulation d'évolution d'investissement sur N années")
    st.sidebar.write("Paramètres")
    init_invest = st.sidebar.number_input("Investissement initial", min_value=0.0, value=1000.0)
    alpha = st.sidebar.slider("Taux de croissance annuelle (%)", min_value=0, max_value=100, value = 3)
    nb_years = st.sidebar.slider("Nombre d'années", min_value=1, max_value=100, value=50)
    add_year = st.sidebar.number_input("Contribution annuelle", min_value=0.0, value=100.0)
    add_month = st.sidebar.number_input("Contribution mensuelle", min_value=0.0, value=0.0)

    # Calcul et affichage des résultats
    invested, evolution = simulate_investment(init_invest, alpha, nb_years, add_year, add_month)
    st.line_chart({"Investi": invested, "Valeur totale": evolution})
    st.write(f"**Somme totale investie:** {'{:,.2f}'.format(np.round(invested[-1], 2))}")
    st.write(f"**Valeur totale du portefeuille:** {'{:,.2f}'.format(np.round(evolution[-1], 2))}")   
    texte_explication = """
    Imaginez que vous avez de l'argent que vous déposez dans une banque ou investissez. Les intérêts composés, c'est comme si cet argent générait des petits revenus, et ensuite ces revenus eux-mêmes généraient à leur tour d'autres revenus. C'est une croissance qui s'accélère au fil du temps. C'est comme une boule de neige qui roule et qui grossit à mesure qu'elle avance. Les intérêts composés font en sorte que votre argent travaille pour vous, et plus le temps passe, plus cette croissance devient importante. C'est un moyen astucieux d'augmenter votre argent au fil des années, simplement en laissant les intérêts s'accumuler et se multiplier.

    Prenons un exemple simple pour mieux comprendre les intérêts composés...
    """
    st.write(texte_explication)

elif language == "English":
    st.title("Investing simulator")
    st.write("Simulation of investment evolution over N years")
    st.sidebar.write("Parameters:")
    init_invest = st.sidebar.number_input("Initial investment", min_value=0.0, value=1000.0)
    alpha = st.sidebar.slider("Annual growth percentage (%)", min_value=0, max_value = 100, value=3)
    nb_years = st.sidebar.slider("Number of years", min_value=1, max_value=100, value=50)
    add_year = st.sidebar.number_input("Annual contribution", min_value=0.0, value=100.0)
    add_month = st.sidebar.number_input("Monthly contribution", min_value=0.0, value=0.0)

    # Calculation and display of results
    invested, evolution = simulate_investment(init_invest, alpha, nb_years, add_year, add_month)
    st.line_chart({"Invested": invested, "Total Value": evolution})
    st.write(f"**Total invested:** {'{:,.2f}'.format(np.round(invested[-1], 2))}")
    st.write(f"**Total value:** {'{:,.2f}'.format(np.round(evolution[-1], 2))}")
    explanation_text = """
    Imagine you have some money that you deposit in a bank or invest. Compound interest is like that money generating small earnings, 
    and then those earnings themselves generating more earnings. It's a growth that accelerates over time. It's like a snowball rolling and 
    getting bigger as it goes. Compound interest makes your money work for you, and as time goes on, this growth becomes more significant. 
    It's a clever way to increase your money over the years, simply by letting the interest accumulate and multiply.
    
    Let's take a simple example to better understand compound interest...
    """
    
    st.markdown(explanation_text)
