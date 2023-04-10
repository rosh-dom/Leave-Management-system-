import pymysql
# import config
from dotenv import load_dotenv
import os


load_dotenv()

conn = pymysql.connect(host=os.environ.get('host_name'),user=os.environ.get('user_name'), password=os.environ.get('user_password'), database=os.environ.get('user_db'))
cur = conn.cursor()

def add_val(description, start_date, end_date):
    add_val=cur.execute("insert into leave_system_management(description, start_date, end_date) values (%s, %s, %s);", ( description, start_date, end_date))
    conn.commit()
    return add_val


def approve_leave(id):

        # status="Sucess"
        approve_leave = cur.execute("update leave_system_management set status= 'Approved' where id=%s", (id))
        conn.commit()
        return approve_leave



def reject_leave(id):

        # status="reject"
        reject_leave=cur.execute("update leave_system_management set status= 'Rejected' where id=%s",(id))
        conn.commit()
        return reject_leave

def delete_value(id):
    delete_id = cur.execute("delete from leave_system_management where id=%s",(id))
    conn.commit()
    return delete_id
    

def display_table():
    cur.execute("select * from leave_system_management")
    conn.commit()
    output = cur.fetchall()


    for i in output:
        print(i)
        
    return output
        # return output

