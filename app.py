from flask import Flask, render_template, request
from Database import Database

app = Flask(__name__)
db = Database()

@app.route('/', methods=["GET", "POST"])
def home():
    # POST request handling
    if request.method == 'POST':
        print("#"*100)
        ttitle = request.form["ttitle"]
        tdesc = request.form["tdesc"]
        print(ttitle)
        print(tdesc)
        db.insertor(ttitle, tdesc)

    # extracting all todos from db
    data = db.fetcher()
    return render_template(
        'index.html', 
        Todos = data
    )

@app.route('/delete/<int:tid>')
def delete(tid):
    return str(tid)

if __name__ == "__main__":
    app.run(debug=True)