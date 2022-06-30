from flask import *
import datetime
import sqlite3
from sqlite3 import Error

db_file = "phone.db"
table = "phonelist"

dum = [
  ('arne', '013-131313'), ('berith','01234'), ('caesar','077-1212321')
]

app = Flask(__name__)

def get_datetime():
    now = datetime.datetime.now()
    current_time = [str(now.hour), str(now.minute)]
    current_date = [str(now.year), str(now.month), str(now.day)]
    if len(current_time[1]) < 2:
        current_time[1] = '0' + current_time[1]
    if len(current_date[1]) < 2:
        current_date[1] = '0' + current_date[1]
    if len(current_date[2]) < 2:
        current_date[2] = '0' + current_date[2]
    return current_date, current_time
    
def find_by_name(tlist, name):
    ret = None
    for idx, entry in enumerate(tlist):
        if entry[0].lower() == name.lower():
            ret = idx, entry
            break
    return ret


@app.route("/")
def start():
    current_datetime = get_datetime()
    return render_template('list.html', list=dum, date=current_datetime[0])

@app.route("/delete")
def delete_entry():
    current_datetime = get_datetime()
    name = request.args["name"]
    deleted_name = None
    to_delete = find_by_name(dum, name)
    if to_delete:
        deleted_name = to_delete[1][0]
        dum.remove(to_delete[1])
    return render_template('delete.html', date=current_datetime[0], time=current_datetime[1], deleted_name=deleted_name)

@app.route("/insert")
def insert_entry():
    current_datetime = get_datetime()
    name = request.args["name"]
    phone = request.args["phone"]
    action = (None, name, phone)
    entry = find_by_name(dum, name)
    if entry:
        idx = entry[0]
        dum[idx] = (name, phone)
        action = ("Modified", name, phone)
    else:
        dum.append((name, phone))
        action = ("Inserted", name, phone)
    #return render_template('list.html', list=dum, date=current_datetime[0])
    return render_template('insert.html', date=current_datetime[0], time=current_datetime[1], performed_action=action)
 