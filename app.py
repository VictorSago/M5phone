from flask import *
import datetime

dum = [
  ('arne', '013-131313'), ('berith','01234'), ('caesar','077-1212321')
]

app = Flask(__name__)

def get_datetime():
    now = datetime.datetime.now()
    current_time = [str(now.hour), str(now.minute)]
    current_date = [str(now.year), str(now.month), str(now.day)]
    if len(current_date[1]) < 2:
        current_date[1] = '0' + current_date[1]
    if len(current_date[2]) < 2:
        current_date[2] = '0' + current_date[2]
    return current_date, current_time
    

@app.route("/")
def start():
    current_datetime = get_datetime()
    return render_template('list.html', list=dum, date=current_datetime[0])

@app.route("/delete")
def delete_entry():
    current_datetime = get_datetime()
    name = request.args["name"]
    deleted = False
    for item in dum:
        if item[0].lower() == name.lower():
            dum.remove(item)
            deleted = True
            break
    if not deleted:
        name = None
    return render_template('delete.html', date=current_datetime[0], time=current_datetime[1], deleted_name=name)

@app.route("/insert")
def insert_entry():
    current_datetime = get_datetime()
    name = request.args["name"]
    phone = request.args["phone"]
    dum.append((name, phone))
    return render_template('insert.html', date=current_datetime[0], time=current_datetime[1], inserted_name=name, inserted_phone=phone)
 