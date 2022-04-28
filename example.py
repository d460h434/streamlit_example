import streamlit as st

#main code
st.title("Hello! this is where the space management app would be")

HR_file = st.file_uploader("This is where users would upload HR data files stored locally on their machine or in approved KU locations",type='csv',)
maximo_file = st.file_uploader("And this is where they would upload the maximo space data files",type='csv')
if HR_file is not None:
    st.write('Thank you for uploading your HR data file!')
    column = st.selectbox("Select a column you would like to pick and value from",list(HR_file.columns.values))
    variable = st.multiselect('select a department',list(HR_file.column.unique()))

if maximo_file is not None:
    st.write('Thank you for uploading your maximo data file!')
    column_two = st.selectbox("Select a column you would like to pick and value from",list(maximo_file.columns.values))
    variable_two = st.multiselect('select a department',list(HR_file.column_two.unique()))





