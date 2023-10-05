import streamlit as st
import pandas as pd

st.title("Streamlit Practice App")
st.write("This is my new app")
button1 = st.button("click me")

if button1:
    st.write("this is some text")

st.header('Start of the checkbox section')
like = st.checkbox("Do you like this app?")
button2 = st.button("Submit")
if button2:
    if like:
        st.write('Thanks, I like it too')
    else:
        st.write("Sorry! You have bad taste")


st.header("Start of the radio button")  # this is a lot like markdown


animal = st.radio("What is your favorite animal?", ("lion", "tiger", "bear"))
button3 = st.button("Submit Animal")
if button3:
    st.write(animal)
    if animal == "lion":
        st.write("Roar!")



st.header("Start of selectbox section")

animal2 = st.selectbox("What animal is your favorite?", ("lion", "tiger", "bear"))
button4 = st.button("Submit Animal2")
if button4:
    st.write(animal2)
    if animal2 == "lion":
        st.write("Roar!")


st.header("Start of multiselect section")
# preserves not only what is selected, but the order that the user have selected them in
options = st.multiselect("What animals do you like?", ["lion", "tiger", "bear"])
button5 = st.button("print animals")
if button5:
    st.write(options)


st.header("Start of the slider section")
epochs_num = st.slider("How many epochs?", 1, 100, 10)  #10 is default argument
if st.button("Slider Button"):
    st.write(epochs_num, type(epochs_num))


st.header("Start of text input section")
user_text = st.text_input("What's your favorite movie?", "Star Wars")  #star wars is default argument
if st.button("text button"):
    st.write(user_text, type(user_text))



user_num = st.number_input("What is your favorite number?")
if st.button("Number button"):
    st.write(user_num, type(user_num))


def run_sentiment_analysis(txt):
    st.write(f'Analysis Done on {txt}')


txt = st.text_area("text to analyze", "it was the best of time, it was the worst of times")
st.write('Sentiment: ', run_sentiment_analysis(txt))


st.header("Import Data")

acuna_df = pd.read_csv("ronald_acuna_stats.csv")
ohtani_df = pd.read_csv("shohei_ohtani_stats.csv")

st.write("Ronald Acuña Jr.")
st.write(acuna_df)
st.write("Shohei Ohtani")
st.write(ohtani_df)


st.write('test')

