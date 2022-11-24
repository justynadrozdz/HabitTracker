import streamlit as st
import pandas as pd
import csv

#Function which returns list of current habits
def check_if_on_list(file):
    csv_list =[]
    with open(file, 'r') as read_obj:
        for row in csv.reader(read_obj):
            csv_list.append(row[0])
    return csv_list


#Function to add habit to csv file
def add_habit(file, sstate):
    csv_list = check_if_on_list(file)
    if sstate and sstate not in csv_list:
        data = {
            'To do:': [sstate]
        }
        csv_list.append(sstate)
        new_to_do = pd.DataFrame(data)
        new_to_do.to_csv(file, mode="a", index=False, header=False)
    return file


#Function to delete habit from csv file
def delete_habit(del_to_do, file):
    df = pd.read_csv(filepath_or_buffer=file, index_col="To do:")
    df = df.drop(df.loc[df.index==del_to_do].index)
    df.to_csv(file)
    return file


#Configuration of page's apperance
st.set_page_config(page_title="To do list", layout="wide")
st.markdown('# To do list')
st.sidebar.markdown("# What are your goals? 😊")
st.sidebar.date_input(label='Today is:')
col1, col2 = st.columns(2)


#First column - Daily to do list
with col1:
    st.header("Daily to do list:")
    csv_file = "../HabitTracker/daily_to_do_list.csv"

    # Adding new daily to do
    with st.form(key="add_to_do", clear_on_submit=True):
        text_input1 = st.text_input("What do you want to do today?", key="to_do", value="")
        s_state = st.session_state["to_do"]
        submit_button1 = st.form_submit_button(label="Add")
        add_habit(csv_file, s_state)

    #Deleting habit
    with st.form(key="del_to_do", clear_on_submit=True):
        text_input2=st.text_input("What do you want to delete from the list?", key="del_to_do", value="")
        submit_button2 = st.form_submit_button(label="Delete")
        if text_input2:
            delete_habit(text_input2,csv_file)
    st.dataframe(pd.read_csv("daily_to_do_list.csv"))


#Second column - Monthly to do list
with col2:
    st.header("Monthly to do list:")
    month_csv_file ="../HabitTracker/to_do_month.csv"

    # Adding new monthly to do
    with st.form(key="to_do_month", clear_on_submit=True):
        text_input3 = st.text_input("What are your monthly goals?", key="to_do_month", value="")
        submit_button3 = st.form_submit_button(label="Add")
        if text_input3:
            s_state_m = st.session_state["to_do_month"]
            add_habit(month_csv_file, s_state_m)

    #Deleting habit
    with st.form(key="del_to_do_month", clear_on_submit=True):
        text_input4=st.text_input("What goal do you want to delete?", key="del_to_do_month", value="")
        submit_button4 = st.form_submit_button(label="Delete")
        if text_input4:
            delete_habit(text_input4,month_csv_file)
    st.dataframe(pd.read_csv("to_do_month.csv"))





