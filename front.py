import streamlit as st
import pandas as pd

st.set_page_config(page_title="Append to Excel", page_icon=":pencil:", layout="wide")

def append_to_excel(date, name, amount):
    df = pd.read_excel("data.xlsx")
    new_row = {"Date": date, "Name": name, "Amount": amount}
    df = df.append(new_row, ignore_index=True)
    df.to_excel("data.xlsx", index=False)

st.title("Append to Excel")

col1, col2, col3 = st.columns(3)

with col1:
    date = st.date_input("Date")

with col2:
    name = st.text_input("Name")

with col3:
    amount = st.number_input("Amount")

if st.button("Append"):
    append_to_excel(date, name, amount)
    st.success("Data appended to Excel sheet!")

if __name__ == "__main__":
    st.write("Enter data to append to Excel sheet.")
