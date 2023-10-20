# https://docs.streamlit.io/library/get-started/installation
# !pip install streamlit
# !streamlit run main_page.py

# Info and documentation https://docs.streamlit.io/library/api-reference


import streamlit as st
import pandas as pd
import numpy as np


def generate_country_real_plan_df(lenght=10, country='UA'):
    df = pd.DataFrame({
        'date': pd.date_range(start='2020-01-01', periods=lenght, freq='D'),
        'country': country,
        'real': np.random.randint(20, 100, lenght)
    })
    df['plan'] = df['real'] + np.random.randint(-10, 100, lenght)
    return df


def add_potential_to_df(df, user_input_coef=1.5):
    df['potential'] = df['plan'] * user_input_coef
    return df


st.title("🚗   Streamlit App Auto   🚜")

st_name = st.text_input('Entere your name please', '')

st.subheader(f'🚀 An awesome data visual app made by {st_name} with love 🚀')

length = st.number_input("Dataframe length", value=10,
                         placeholder="Type a number...")
st.write('Dataframe length is ', length)

country = st.selectbox(
    "Country name",
    ("Ukraine", "England", "USA", "Germany", "Poland"),
    placeholder="Select country",
)

st.write('You selected:', country)

df = generate_country_real_plan_df(length, country)


col1, col2 = st.columns(2)
with col1:
    df
with col2:
    st.dataframe(df)


coef = st.number_input("Coef", value=1.5, step=0.1,
                       placeholder="Type a coeficient...")
st.write('Coeficient is ', coef)

df_potential = add_potential_to_df(df, coef)

st.subheader('Dataframe with potential')
st.dataframe(df_potential)

plan_acheivement = np.sum(df.real) / np.sum(df.plan)

st.write('Plan achievment is:')
plan_acheivement


potential_acheivement = np.sum(df.real) / np.sum(df.potential)

st.write('Potential achievment is:')
potential_acheivement


st.line_chart(
    df_potential, x='date', y=['real', 'plan', 'potential'], color=["#FF0000", "#0000FF", "#00ff00"]
)


# 10*. Extra tasks: User input 3 country names (or N countries)
# Show plan and real values for all countries together
# Show plan and real values for each country separately

countries = st.multiselect(
    "Country names",
    ("Ukraine", "England", "USA", "Germany", "Poland"),
    placeholder="Select country",
)

country_df = pd.DataFrame()


for country in countries:
    df_country = generate_country_real_plan_df(length, country)
    country_df['date'] = df_country.date
    country_df[f'{country}_plan'] = df_country['plan']
    country_df[f'{country}_real'] = df_country['real']


all_countries = st.checkbox('All together')

if not country_df.empty:
    if all_countries:
        st.dataframe(country_df)
        st.line_chart(country_df, x='date', y=list(country_df.columns))
    else:
        for country in countries:
            st.subheader(country)
            st.line_chart(country_df, x='date', y=(
                f'{country}_plan', f'{country}_real'))

# Task
# 1. Write Title and Subtitle on the page 🚀
# 2. User input dataframe lenght and country name 🚀
# 3. Generate dataframe with selected lenght and country name 🚀
# 4. User input coef for potential column 🚀
# 5. Add column 'potential' to dataframe 🚀
# 6. Show dataframe on the page 🚀
# 7. Show plan acheivement ( sum(real) / sum(plan) ) 🚀
# 8. Show potential acheivement ( sum(real) / sum(potential) ) 🚀
# 9. Show plot with real, plan and potential values 🚀

# 10*. Extra tasks: User input 3 country names (or N countries) 🚀
# Show plan and real values for all countries together 🚀
# Show plan and real values for each country separately 🚀


# Watched whole playlist about Streamlit: https://www.youtube.com/watch?v=7yFh9dBtSko&list=PLavJpcg8cl1FA5cmCfdzdHyOBVT6VLhQX
