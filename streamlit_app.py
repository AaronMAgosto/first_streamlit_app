import streamlit  

streamlit.title('My Parents New Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🥣 omega 3 & blueberry oatmeal')
streamlit.text('🥗 kale, sinach, & rocket smoothie')
streamlit.text('🐔 hard-boilded free range egg')
streamlit.text('🥑🍞avacado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)




