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
    error = None
    meth = request.method
    ''' if request.method == "DELETE":
        name = request.form["name"]
        for item in dum:
            if item[0].lower() == name.lower():
                dum.remove(item)
                break
        return render_template('delete.html', list=dum, date=current_date, deleted=name, error=error) '''
    name = request.args["name"]
    for item in dum:
        if item[0].lower() == name.lower():
            dum.remove(item)
            break
    return render_template('delete.html', date=current_date, deleted=name, error=error, method=meth)
    #return render_template('list.html', list=dum, date=current_date)
