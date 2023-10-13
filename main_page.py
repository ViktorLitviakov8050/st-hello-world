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
    df['plan'] = df['real'] + np.random.randint(-10, 10, lenght)
    return df

def add_potential_to_df(df, user_input_coef=1.1):
    df['potential'] = df['plan'] * user_input_coef
    return df


st.title("Streamlit App")

st.subheader("An awesome data visualization app made by Viktor)")


# Task
# 1. Write Title and Subtitle on the page
# 2. User input dataframe lenght and country name
# 3. Generate dataframe with selected lenght and country name
# 4. User input coef for potential column
# 5. Add column 'potential' to dataframe
# 6. Show dataframe on the page
# 7. Show plan acheivement ( sum(real) / sum(pred) )
# 8. Show potential acheivement ( sum(real) / sum(potential) )
# 9. Show plot with real, plan and potential values

# 10*. Extra tasks: User input 3 country names (or N countries)
# Show plan and real values for all countries together 
# Show plan and real values for each country separately



# Watched whole playlist about Streamlit: https://www.youtube.com/watch?v=7yFh9dBtSko&list=PLavJpcg8cl1FA5cmCfdzdHyOBVT6VLhQX
