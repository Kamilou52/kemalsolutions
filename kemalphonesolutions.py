import sqlite3
from flask import Flask, render_template, session, url_for, request, redirect, abort
from flask_session import Session
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

app = Flask('kemalphonesolutions')
app.secret_key = "super secret key"
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False


def get_db_connection():
    conn = sqlite3.connect('static/database.db')
    sql = sqlite3
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home_page():

    return render_template('indexkemalphones.html')

@app.route("/contactus")
def send():

    return render_template('contactus.html')

@app.route("/testing")
def seetest():
    return render_template("testing.html")

@app.route("/flutterapp")
def view():
    return render_template("flutterapp.html")

@app.route("/ionicapp")
def viewio():
    return render_template("ionicapp.html")

@app.route("/userinput", methods=["GET","POST"])
def seeuser():
    if request.method == 'POST':
        session['userinput'] = request.form['fname']
        return render_template("androidapp.html")

    return render_template('userinput.html')

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#      if request.method == 'POST':
#         file = request.files['the_file']
#         file.save('/var/www/uploads/uploaded_file.txt')
#         #file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
# redirect(url_for("searchmodelmac"))

@app.route('/androidapp', methods=['GET', 'POST'])
def searchmodel():
    if request.method == "POST":
        fname=request.form.get("fname")
        session.pop('fname', None)
        modele=request.form.get("modele")
        session.pop('modele', None)
        modeles=request.form.get("modeles")
        session.pop('modeles', None)
        Problems=request.form.get("Problems")
        session.pop('problem', None)


        session['fname'] = fname
        session['modeles'] = modele
        session['problem'] = Problems
        store(session['userinput'],modele,Problems)

        return search_userinput()

        # return render_template('indexkemalphones.html', modele=modeles)

    return render_template("androidapp.html")

@app.route("/iOSapp", methods=['GET', 'POST'])
def searchmodelmac():
    if request.method == "POST":
        fname=request.form.get("fname")
        session.pop('fname', None)
        modele=request.form.get("modele")
        session.pop('modele', None)
        modeles=request.form.get("modeles")
        session.pop('modeles', None)
        Problems=request.form.get("Problems")
        session.pop('problem', None)

        session['fname'] = fname
        session['modeles'] = modele
        session['problem'] = Problems

        store(session['userinput'],modele,Problems)

        return search_userinput()
        # return render_template("indexkemalphones.html", modele=modeles)

    return render_template("iOSapp.html")


def store(userinput,modele,problem):
    conn = get_db_connection()

    data=[userinput, modele, problem ]

    val = conn.execute('insert into userinput (fname, modele, problem, created ) values (?,?,?,datetime())', data)
    print (val)

    conn.commit()

    conn.close()
    if userinput is None:
        abort(404)

    return userinput

@app.route('/indexkemalphones', methods=["GET", "POST"])
def liste():

    conn = get_db_connection()
    resultat = conn.execute('SELECT * FROM userinput').fetchall()
    conn.close()
    return render_template('indexkemalphones.html', userinputs=resultat)

# def list(userinput):
#     conn = get_db_connection()
#     userinput1 = userinput1.query.filter_by(fname='testuser').first()
    # data=[userinput ]
    # value = conn.execute('SELECT * FROM userinput ',
    #                     (userinput,)).fetchone()
    # print(value)

    # print(data)
#     print(userinput1)

    # conn.close()
    # if userinput is None:
    #     abort(404)
#     return userinput[1]

# List userinputs with filter

def search_userinput():
     conn = get_db_connection()
     # filtre ='%'+modele+"%"
     resultat = conn.execute('select * from userinput , sqlite_sequence where id = seq ', [filtre,]).fetchall()

     conn.close()

     if modele is None:
         abort(404)

     return render_template('indexkemalphones.html', userinputs=resultat)



# def get_list_userinput_connection():
#     conn = sqlite3.connect('static/list_userinput.txt')
#     conn.row_factory = sqlite3.Row
#     return conn

# @app.route('/userinput_list')
# def list(userinput):
#     sql = sqlite3
#     conn = sql.connect('templates/userinput_list')
#     conn.session_factory = sql.Session

#     cur = conn.cursor()
#     value = conn.execute('SELECT * FROM userinput WHERE id = ?',
#                          (userinput,)).fetchone()
#     sessions = cur.fetchall();
#     return render_template("userinput_list.html",sessions = sessions)


@app.route("/mission")
def viewmis():
    return render_template("mission.html")

@app.route("/vision")
def viewvis():
    return render_template("vision.html")

@app.route("/team")
def viewte():
    return render_template("team.html")

@app.route("/congratulations")
def viewcong():
    return render_template("congratulations.html")

@app.route("/socialmedia")
def visit():
    return render_template("socialmedia.html")

@app.route("/webdesigning")
def viewebdes():
    return render_template("webdesigning.html")

if __name__ == "__main__":
    app.run(debug=True)
