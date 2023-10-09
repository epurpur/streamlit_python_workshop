import streamlit as st
import pandas as pd

# Basic title and text on the screen
st.title("Streamlit Practice App")
st.write("This is my new app")
button1 = st.button("click me")
#anotherButton = st.button("click me")   #this won't work. Each button needs to have different text

# Buttons
if button1:
    st.write("this is some text")
st.write('---')

# Markdown
st.header("Markdown Section")
st.markdown("""
This is markdown!
# Big Markdown Title
## Medium Markdown Title
### Small Markdown Title
You can do **a lot** of *other stuff* in markdown including images, videos, etc

---
""")

# Checkboxes
st.header('Checkbox section')
like = st.checkbox("Do you like this app?")
button2 = st.button("Submit")
if button2:
    if like:
        st.write('Thanks, I like it too')
    else:
        st.write("Sorry! You have bad taste")

st.write('---')

# Radio Button
st.header("Radio button section")  # this is a lot like markdown

animal = st.radio("What is your favorite animal?", ("lion", "tiger", "bear"))
button3 = st.button("Submit Animal")
if button3:
    st.write(animal)
    if animal == "lion":
        st.write("Roar!")

st.write('---')


# Select Box
st.header("Selectbox section")

animal2 = st.selectbox("What animal is your favorite?", ("lion", "tiger", "bear"))
button4 = st.button("Submit Animal2")
if button4:
    st.write(animal2)
    if animal2 == "lion":
        st.write("Roar!")

st.write('---')

# Multi Select Box

st.header("Multiselect section")
# preserves not only what is selected, but the order that the user have selected them in
options = st.multiselect("What animals do you like?", ["lion", "tiger", "bear"])
button5 = st.button("print animals")
if button5:
    st.write(options)

st.write('---')

# Slider

st.header("Slider section")
epochs_num = st.slider("How many epochs?", 1, 100, 10)  #10 is default argument
if st.button("Slider Button"):
    st.write(epochs_num, type(epochs_num))

st.write('---')

# Text Input

st.header("Text input section")
user_text = st.text_input("What's your favorite movie?", "Star Wars")  #star wars is default argument
if st.button("text button"):
    st.write(user_text, type(user_text))

st.write('---')

# Number button
st.header("Number Button section")
user_num = st.number_input("What is your favorite number?")
if st.button("Number button"):
    st.write(user_num, type(user_num))

st.write('---')

# Write your own functions

st.header("Write your own function")

def multiplier_function(number):
    st.write("User choice: ", number)
    st.write(f'Number multiplied = {number * 2}')

number_choice = st.number_input('Choose a number')
function_button = st.button('Multiply the number!')
if function_button:
    multiplier_function(number_choice)

st.write('---')

# Import a dataset
st.header("Import Data")

st.write("Here I am importing a couple of simple .csv files. These are the statistics for two major league baseball players")
acuna_df = pd.read_csv("ronald_acuna_stats.csv")
ohtani_df = pd.read_csv("shohei_ohtani_stats.csv")

#convert the year column to an string so it displays better
acuna_df['Year'] = acuna_df['Year'].astype(str)
ohtani_df['Year'] = ohtani_df['Year'].astype(str)

st.write("Ronald Acuña Jr.")
st.write(acuna_df)
st.write("Shohei Ohtani")
st.write(ohtani_df)

#filter on the fly
st.write('You can filter datasets on the fly at the press of a button')
st.selectbox('More or less than 40 HR?', ('More', 'Less'))

home_runs = st.selectbox('Do you want to stats for years with more or less than 40 HR?', ('More', 'Less'))
hr_button = st.button('Go!')

if hr_button:
    if home_runs == 'More':
        # more than 40 HR
        acuna_modified = acuna_df.loc[acuna_df['HR'] > 40]
        ohtani_modified = ohtani_df.loc[ohtani_df['HR'] > 40]
        st.write("Acuña modified")
        st.write(acuna_modified)
        st.write("Ohtani modified")
        st.write(ohtani_modified)
    else: 
        # less than 40 HR
        acuna_modified = acuna_df.loc[acuna_df['HR'] < 40]
        ohtani_modified = ohtani_df.loc[ohtani_df['HR'] < 40]
        st.write("Acuña modified")
        st.write(acuna_modified)
        st.write("Ohtani modified")
        st.write(ohtani_modified)

st.write('---')



# Maps
import numpy as np

df = pd.DataFrame(
    # creates 10 random points in and around Charlottesville
    np.random.randn(10, 2) / [50, 50] + [38.033, -78.507],
    columns=['lat', 'lon'])

st.write(df)
st.map(df)

