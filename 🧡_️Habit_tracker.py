import streamlit as st
import pandas as pd


def show_habits():
    df = pd.read_csv("habits.csv")

    for row in df:

        st.write(row)




    #reading file to streamlit checkbox view
    # for line in df:
    #     i=0
    #     for item in line:
    #         if item == False:
    #             item = st.checkbox(i, False)
    #             st.write(item)
    #
    #             i+=1
    #
    #         elif item == True:
    #             # item.checkbox(key=f"{i+1}", value=True)
    #             i += 1
    #         else:
    #             st.checkbox(label="")
    return df


def add_habit():
    csv_file = pd.read_csv("habits.csv")
    csv_db = pd.DataFrame(csv_file)
    if st.session_state["habit"] and st.session_state["habit"] not in csv_db["Habit"].to_list():
        data = {
            'Habit': [st.session_state.habit],
            'Mon': False,
            'Tue': False,
            'Wed': False,
            "Thu": False,
            "Fri": False,
            "Sat": False,
            "Sun": False
        }

        new_habit = pd.DataFrame(data)
        new_habit.to_csv("habits.csv", mode="a", index=False, header=False)


def delete_habit(del_habit):
    df = pd.read_csv("habits.csv", index_col="Habit")
    df = df.drop(df.loc[df.index==del_habit].index)
    df.to_csv("habits.csv")



st.set_page_config(page_title="Habit Tracker", layout="wide")

st.markdown('# Habit Tracker')
st.sidebar.markdown("# Habit Tracker")


# Adding new habit
with st.form(key="add_habit", clear_on_submit=True):
    text_input=st.text_input("What habit do you want to track?", key="habit", value="")
    submit_button = st.form_submit_button(label="Add habit")
    add_habit()


#Deleting habit
with st.form(key="del_form", clear_on_submit=True):
    text_input=st.text_input("What habit do you want to delete?", key="del_habit", value="")
    submit_button = st.form_submit_button(label="Delete habit")
    delete_habit(text_input)



st.dataframe(show_habits())





