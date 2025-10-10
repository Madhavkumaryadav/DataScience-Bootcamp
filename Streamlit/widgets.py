import streamlit as st
import pandas as pd

st.title("Streamlit Text Input ")
name=st.text_input("Enter Your Name ")

age=st.slider('Select Your Age : ',0,100,25)

st.write(f'Your age is {age}')

options=['python','java','c++','javaScript']
choice=st.selectbox('Choose your favorite  language : ',options)
st.write(f'You Selected {choice}')


if name:
    st.write(f'Hello , {name}')


data={
    'Name':['madhav','suraj','subodh','vishal'],
    'age':[23,43,23,54],
    'City':['new york','syden','france','england']
}

df=pd.DataFrame(data)
df.to_csv('sample.csv')

st.write(df)

uploaded_file=st.file_uploader('Chose a csv file ' , type='csv')

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)
    
    