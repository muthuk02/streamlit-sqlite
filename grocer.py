import streamlit as st
import sqlite3

st.title("Money Manager")

conn = sqlite3.connect("site.db")
cursor = conn.cursor()

def main():
    st.write("Please update your expenses list:")
    with st.form(key="Today's Log"):
        log_date = st.date_input("Date:")
        user_name = st.text_input("User Name:", value="muthuk")
        currency_code = st.selectbox("Currency Code", ['SGD', 'INR'])
        category = st.selectbox("Category", ['Groceries', 'Food', 'Bills', 'Transport', 'Travel'])
        sub_category = st.selectbox("choose")
        submit = st.form_submit_button(label="Submit")



if __name__ == '__main__':
    main()
