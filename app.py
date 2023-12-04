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
    montrer_guide = st.button("Afficher le guide")
    st.sidebar.write("**Paramètres**")
    init_invest = st.sidebar.number_input("Investissement initial", min_value=0.0, value=1000.0)
    alpha = st.sidebar.slider("Taux de croissance annuelle (%)", min_value=0, max_value=100, value = 3)
    nb_years = st.sidebar.slider("Nombre d'années", min_value=1, max_value=100, value=50)
    add_year = st.sidebar.number_input("Contribution annuelle", min_value=0.0, value=100.0)
    add_month = st.sidebar.number_input("Contribution mensuelle", min_value=0.0, value=0.0)

    # Guide
    if montrer_guide:
        st.subheader("Guide explicatif")
        texte_explication = """
        Imaginez que vous avez de l'argent que vous déposez dans une banque ou investissez. Les intérêts composés, c'est comme si cet argent générait des petits revenus, et ensuite ces revenus eux-mêmes généraient à leur tour d'autres revenus. C'est une croissance qui s'accélère au fil du temps. C'est comme une boule de neige qui roule et qui grossit à mesure qu'elle avance. Les intérêts composés font en sorte que votre argent travaille pour vous, et plus le temps passe, plus cette croissance devient importante. C'est un moyen astucieux d'augmenter votre argent au fil des années, simplement en laissant les intérêts s'accumuler et se multiplier.
    
        Prenons un exemple simple pour mieux comprendre les intérêts composés. Imaginons que vous investissiez 100 € à un taux d'intérêt de 5 % par an. Après la première année, vous auriez 105 € (votre capital initial de 100 € plus 5 € d'intérêts).
    
        Maintenant, au lieu de retirer ces 5 €, vous décidez de les laisser dans l'investissement. L'année suivante, le taux d'intérêt s'applique non seulement à votre capital initial de 100 €, mais aussi aux 5 € d'intérêts de l'année précédente. Ainsi, à la fin de la deuxième année, vous auriez 110,25 € (100 € + 5 € + 5,25 € d'intérêts).
        
        Vous pouvez voir comment, avec les intérêts composés, les gains de chaque année sont ajoutés à votre capital, et les intérêts s'accumulent sur l'ensemble du montant, non seulement sur la somme initiale. Au fil des années, cet effet d'accumulation devient de plus en plus significatif, créant une croissance exponentielle de votre investissement. C'est la magie des intérêts composés en action.
        """
        st.markdown(texte_explication)
    
    # Calcul et affichage des résultats
    invested, evolution = simulate_investment(init_invest, alpha, nb_years, add_year, add_month)
    st.subheader("Graphique")
    st.write(f"Simulation d'évolution d'investissement sur {nb_years} année(s)")
    st.line_chart({"Investi": invested, "Valeur totale": evolution})
    st.write(f"**Somme totale investie:** {'{:,.2f}'.format(np.round(invested[-1], 2))}")
    st.write(f"**Valeur totale du portefeuille:** {'{:,.2f}'.format(np.round(evolution[-1], 2))}")   

elif language == "English":
    st.title("Investing simulator")
    show_guide = st.button("Show Guide")
    st.sidebar.write("**Parameters**")
    init_invest = st.sidebar.number_input("Initial investment", min_value=0.0, value=1000.0)
    alpha = st.sidebar.slider("Annual growth percentage (%)", min_value=0, max_value = 100, value=3)
    nb_years = st.sidebar.slider("Number of years", min_value=1, max_value=100, value=50)
    add_year = st.sidebar.number_input("Annual contribution", min_value=0.0, value=100.0)
    add_month = st.sidebar.number_input("Monthly contribution", min_value=0.0, value=0.0)

    # Calculation and display of results
    invested, evolution = simulate_investment(init_invest, alpha, nb_years, add_year, add_month)

    #Guide
    if show_guide:
        st.subheader("Explanatory Guide")
        explanation_text = """
        Imagine you have some money that you deposit in a bank or invest. Compound interest is like that money generating small earnings, 
        and then those earnings themselves generating more earnings. It's a growth that accelerates over time. It's like a snowball rolling and 
        getting bigger as it goes. Compound interest makes your money work for you, and as time goes on, this growth becomes more significant. 
        It's a clever way to increase your money over the years, simply by letting the interest accumulate and multiply.
        
        Let's take a simple example to better understand compound interest. Suppose you invest \$100 at an interest rate of 5% per year. After the first year, you would have \$105 (your initial capital of \$100 plus \$5 in interest).
    
        Now, instead of withdrawing that \$5, you decide to leave it in the investment. The next year, the interest rate applies not only to your initial capital of \$100 but also to the \$5 in interest from the previous year. So, at the end of the second year, you would have \$110.25 (\$100 + \$5 + \$5.25 in interest).
        
        You can see how, with compound interest, the gains from each year are added to your capital, and interest accumulates on the entire amount, not just the initial sum. Over the years, this compounding effect becomes increasingly significant, creating exponential growth in your investment. That's the magic of compound interest in action.
        """
        st.markdown(explanation_text)

    # Charts
    st.subheader("Chart")
    st.write(f"Investment evolution simulation over {nb_years} year(s)")
    st.line_chart({"Invested": invested, "Total Value": evolution})
    st.write(f"**Total invested:** {'{:,.2f}'.format(np.round(invested[-1], 2))}")
    st.write(f"**Total value:** {'{:,.2f}'.format(np.round(evolution[-1], 2))}")
