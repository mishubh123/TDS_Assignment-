import streamlit as st

st.title("Find the largest among the 3 numbers")

numl = st.number input("Enter number 1")
num2 = st.number input ("Enter number 2")
num3 = st.number input("Enter number 3")

calculate = st.button("Find largest number")

def largest number (a, b, c):
if a > b and a > c:
return a
elif b > a and b > c:
return b
else:
return c

if calculate:

largest num = largest number (numl, num2,
num3)

st.write("The largest number is:",
largest num)
