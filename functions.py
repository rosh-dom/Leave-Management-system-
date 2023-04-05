import pymysql
import config
from dotenv import load_dotenv
import os

load_dotenv()

conn = pymysql.connect(host=os.environ.get('host_name'),user=os.environ.get('user_name'), password=os.environ.get('user_password'), database=os.environ.get('user_db'))
cur = conn.cursor()

def add_val(id, description, start_date, end_date):
    cur.execute("insert into leave_systems(id, description, start_date, end_date,status) values (%s, %s, %s, %s);", (id, description, start_date, end_date))
    conn.commit()


def approve_leave(id):

        # status="Sucess"
        cur.execute("update leave_systems set status= 'Approved' where id=%s", id)
        conn.commit()



def reject_leave(id):

        # status="Sucess"
        cur.execute("update leave_systems set status= 'Rejected' where id=%s",id)
        conn.commit()


def display_table():
    cur.execute("select * from leave_systems")
    output = cur.fetchall()

    for i in output:
        print(i)
