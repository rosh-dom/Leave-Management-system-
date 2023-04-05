# %%
pip install pymysql


# %%


# %%
import pymysql
# import mysql.connector

conn = pymysql.connect(host="training.cqymaactdeez.us-east-1.rds.amazonaws.com",
user="admin", password="MsqlTrain123", database="training")

# %%

# cur.close()
cur = conn.cursor()

# %%
def add_val(id, description, start_date, end_date):
    cur.execute("insert into leave_systems(id, description, start_date, end_date,status) values (%s, %s, %s, %s);", (id, description, start_date, end_date))
    conn.commit()
    

# %%
#add_val(4,"Vacation", "7th April", "8th April", "Pending")

# %%
# add_val(7,"Vacation", "7th April", "9th April","pending")
# add_val(8,"Vacation", "7th April", "10th April","pending")
# add_val(9,"Vacation", "7th April", "11th April","pending")

# %%
def approve_leave(id):

        # status="Sucess"
        cur.execute("update leave_systems set status= 'Approved' where id=%s", id)
        conn.commit()


# %%
approve_leave(4)


# %%
def reject_leave(id):

        # status="Sucess"
        cur.execute("update leave_systems set status= 'Rejected' where id=%s",id)
        conn.commit()

# %%
reject_leave(7)

# %%
cur = conn.cursor()
def display_table():
    cur.execute("select * from leave_systems")
    output = cur.fetchall()

    for i in output:
        print(i)




# %%
display_table()

# %%



