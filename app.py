import streamlit as st
from workout_logs import WorkoutLogs
import sqlite3

st.title("Daily Workout Logs")

conn = sqlite3.connect("site.db")
cur = conn.cursor()

log = WorkoutLogs(
    log_date= st.date_input("Date:"),
    user_name= st.text_input("User Name:", value="muthuk"),
    current_weight= st.text_input("Enter current weight:"),
    calories_intake= st.text_input("Calories Taken:"),
    calories_burned= st.text_input("Calories Burned:")
)

def main():
    # create table
    create_table()

    
    # with st.form(key="Today's Log"):
    log_date = log.log_date
    user_name = log.user_name
    current_weight = log.current_weight
    calories_intake = log.calories_intake
    calories_burned = log.calories_burned
    submit = st.form_submit_button(label="Submit")

    if submit == True:
        conn.execute(f"select * from workout_logs where user_name = '{user_name}' and log_date = '{log_date}'")
        results = cur.fetchone()
        
        if results != None:
            st.warning("Your logs already updated in the system!")
        else:
            # sql = f"insert into workout_logs(log_date, user_name, current_weight, calories_intake, calories_burned) values({log_date}, '{user_name}', {current_weight}, {calories_intake}, {calories_burned})"
            insert_log(log)
            st.success("Data has been added successfully!")
    else:
        pass
        # st.error("Something went wrong, please try again")

    cur.close()
    conn.close()



def create_table():
    sql_query = """
    create table if not exists workout_logs(
        id integer primary key autoincrement,
        log_date timestamp not null,
        user_name text not null,
        current_weight float not null,
        calories_intake float,
        calories_burned float,
        constraint workout_logs_const unique (log_date, user_name)
    );
"""
    cur.execute(sql_query)
    return print(f"Table has been created successfully!\n {sql_query}")

def get_logs(log_date):
    cur.execute("select * from workout_logs where log_date = :log_date", {'log_date': log_date})
    return cur.fetchall()

def insert_log(log):
    with conn:
        cur.execute("insert into workout_logs (log_date, user_name, current_weight, calories_intake, calories_burned) \
                    values (:log_date, :user_name, :current_weight, :calories_intake, :calories_burned)", \
                    {'log_date':log.log_date, 'user_name':log.user_name, 'current_weight':log.current_weight, \
                     'calories_intake':log.calories_intake, 'calories_burned':log.calories_burned})

def remove_log(log):
    with conn:
        cur.execute("delete from workout_logs where log_date = :log_date", {log.log_date})

def update_log(log, log_date, current_weight, calories_intake, calories_burned):
    with conn:
        cur.execute("update workout_logs set  = :current_weight, :calories_intake, :calories_burned where log_date = :log_date)", \
                     {'current_weight': log.current_weight, 'calories_intake': log.calories_intake, \
                      'calories_burned': log.calories_burned, 'log_date': log.log_date })

if __name__ == '__main__':
    main()

