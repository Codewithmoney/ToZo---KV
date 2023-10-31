from flask import Flask, redirect, render_template, request
from Database import Database

app = Flask(__name__)
db = Database()

@app.route('/', methods=["GET", "POST"])
def home():
    # POST request handling
    if request.method == 'POST':
        ttitle = request.form["ttitle"]
        tdesc = request.form["tdesc"]
        db.creater(ttitle, tdesc)

    # extracting all todos from db
    Todos = db.reader()
    return render_template(
        'index.html', 
        Todos = Todos
    )

@app.route('/update/<int:tid>', methods=['GET', 'POST'])
def update(tid):
    if request.method == "POST":
        ttitle = request.form["ttitle"]
        tdesc = request.form["tdesc"]
        db.updater(tid, ttitle, tdesc)
        return redirect("/")

    data = db.reader()
    Todos = None
    for d in data:
        if d['tid'] == tid:
            Todos = d

    return render_template("update.html", Todos=Todos)

@app.route('/delete/<int:tid>')
def delete(tid):
    db.deleter(tid)
    return redirect("/")

@app.route('/deleteAll')
def deleteAll():
    db.deleter("all")
    return redirect("/")

if __name__ == "__main__":
    app.run()