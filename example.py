import streamlit as st
import pandas as pd
import streamlit as st

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    #main code
    st.title("Hello! this is where the space management app would be")

    HR_file = st.file_uploader("This is where users would upload HR data files stored locally on their machine or in approved KU locations",type='csv',)

    maximo_file = st.file_uploader("And this is where they would upload the maximo space data files",type='csv')

    if HR_file is not None:
        HR_file=pd.read_csv(HR_file)
        st.write('Thank you for uploading your HR data file!')
        column = st.selectbox("Select a column you would like to pick and value from",list(HR_file.columns.values))
        if column is not None:
            variable = st.multiselect('select a department',list(HR_file.loc[:,column]))

    if maximo_file is not None:
        maximo_file=pd.read_csv(maximo_file)
        st.write('Thank you for uploading your maximo data file!')
        column_two = st.selectbox("Select a column you would like to pick and value from",list(maximo_file.columns.values))
        if column_two is not None:
            variable_two = st.multiselect('select a department',list(maximo_file.loc[:,column_two]))




