from flask import *
import datetime

dum = [
  ('arne', '013-131313'), ('berith','01234'), ('caesar','077-1212321')
]

app = Flask(__name__)

@app.route("/")
def start():
    now = datetime.datetime.now()
    current_date = [str(now.year), str(now.month), str(now.day)]
    if len(current_date[1]) < 2:
        current_date[1] = '0' + current_date[1]
    if len(current_date[2]) < 2:
        current_date[2] = '0' + current_date[2]
    return render_template('list.html', list=dum, date=current_date)

@app.route("/delete")
def delete_entry():
    now = datetime.datetime.now()
    current_date = [str(now.year), str(now.month), str(now.day)]
    current_time = [str(now.hour), str(now.minute)]
    if len(current_date[1]) < 2:
        current_date[1] = '0' + current_date[1]
    if len(current_date[2]) < 2:
        current_date[2] = '0' + current_date[2]
    error = None
    meth = request.method
    name = request.args["name"]
    deleted = False
    for item in dum:
        if item[0].lower() == name.lower():
            dum.remove(item)
            deleted = True
            break
    if not deleted:
        name = None
    return render_template('delete.html', date=current_date, time=current_time, deleted_name=name, error=error, method=meth)

@app.route("/insert")
def insert_entry():
    now = datetime.datetime.now()
    current_date = [str(now.year), str(now.month), str(now.day)]
    current_time = [str(now.hour), str(now.minute)]
    if len(current_date[1]) < 2:
        current_date[1] = '0' + current_date[1]
    if len(current_date[2]) < 2:
        current_date[2] = '0' + current_date[2]
    error = None
    name = request.args["name"]
    phone = request.args["phone"]
    dum.append((name, phone))
    return render_template('insert.html', date=current_date, time=current_time, inserted_name=name, inserted_phone=phone, error=error)
 