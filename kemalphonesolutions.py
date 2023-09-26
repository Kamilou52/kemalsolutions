import sqlite3
from flask import Flask, g, render_template, session, url_for, request, flash, redirect, make_response, abort, jsonify
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
    # conn = sqlite3.connect('static/database.db')
    # cursor = conn.cursor()
    
    return conn

# Alter the table to remove the NOT NULL constraint on fname column
# cursor.execute("PRAGMA foreign_keys = OFF")
# cursor.execute("BEGIN TRANSACTION")
# cursor.execute("CREATE TABLE userinput_new (id INTEGER PRIMARY KEY, fname TEXT, lname TEXT, medele TEXT, problem TEXT)")
# cursor.execute("INSERT INTO userinput_new SELECT * FROM userinput")
# cursor.execute("DROP TABLE userinput")
# cursor.execute("ALTER TABLE userinput_new RENAME TO userinput")
# cursor.execute("COMMIT")
# cursor.execute("PRAGMA foreign_keys = ON")

# conn.close()

# conn = sqlite3.connect('your_database.db')
# cursor = conn.cursor()

# Alter the table to provide a default value for fname column
# cursor.execute("ALTER TABLE userinput ALTER COLUMN fname SET DEFAULT 'Unknown'")

# conn.close()



# def get_db_connection():
    # conn = sqlite3.connect('static/database.db')
    # sql = sqlite3
    # data=[userinput, modele, problem ]
    # conn.row_factory = sqlite3.Row
    # cursor = conn.cursor()
    
    # try:
    # # Insert a row with a non-null value for fname
    
    # data=conn.execute('insert into userinput(fname, modele, problem, created ) values (?,?,?,datetime())', data)
    
    # conn = sqlite3.connect('static/database.db')
    # if conn.closed:
        
    #     conn = sqlite3.connect('static/database.db')
        

    # except sqlite3.IntegrityError as e:
    # Close the database connection
    # conn.commit()
    
    # conn.close()
    # return conn

@app.route('/')
def home_page():
    fname = request.args.get("userinput")
    if fname == request.cookies.get('fname'):
        resp = make_response(render_template('indexkemalphones.html'))
        resp.set_cookie('fname', 'the fname')
        return render_template('indexkemalphones.html')
    
    return resp

# @app.route('/submit', methods=['POST'])
# def submit():
#     fname = request.form.get('userinput')
    
#     if not fname.isalpha():
#         flash('Please enter only alphabetic letters.')
#         return (redirect("userinput.html"))
#     else:
#     # Process the valid input here
#      flash('Input successfully submitted!')
#     return render_template("androidapp.html")

@app.route("/userinput", methods=["GET","POST"])
def seeuser():
    if request.method == 'POST':
        session['userinput'] = request.form['fname']
        return render_template("androidapp.html")

    return render_template('userinput.html')

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


        session['userinput'] = fname
        session['modele'] = modele
        session['problem'] = Problems
        print("Bonjour")
        store(session['userinput'],modele,Problems)
        print("Hello")
        return search_userinput()
      
        # return render_template("androidapp.html")

    return render_template("indexkemalphones.html")

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

        session['userinput'] = fname
        session['modele'] = modele
        session['problem'] = Problems

        store(session['userinput'],modele,Problems)
        
        # return search_userinput()
        # return redirect(url_for(home_page()))
        return render_template("indexkemalphones.html")

    return render_template("iOSapp.html")


def store(userinput,modele,problem):
    conn = get_db_connection()
    
    print (userinput)

    data=[userinput, modele, problem ]

    val = conn.execute('insert into userinput (fname, modele, problem, created ) values (?,?,?,datetime())', data)
    
    print ( val) 
    

    conn.commit()

    conn.close()
    if userinput is None:
        abort(404)

    return userinput

@app.route('/indexkemalphones', methods=["GET", "POST"])
def liste():

    conn = get_db_connection()
    resultat = conn.execute('SELECT * FROM userinput').fetchall()
    
    # conn.commit()
    conn.close()
    return render_template('indexkemalphones.html', userinputs=resultat)

def search_userinput():
     conn = get_db_connection()
    
     resultat = conn.execute('select * from userinput , sqlite_sequence where id = seq ').fetchall()

    #  conn.commit()
     
     conn.close()

     return render_template('indexkemalphones.html', userinputs=resultat)

@app.route("/me")
def me_api():
    userinput = seeuser('userinput')
    return {
        "fname": userinput.fname,
        "modele": userinput.modele,
        "problem": url_for("seeuser", filename=seeuser),
    }

@app.route("/userinput_list")
def users_api():
    userinputs = seeuser()
    return jsonify([userinput.to_json() for userinput in userinputs])
 
# @app.route('/', methods=["GET", "POST"])
# def list():
    # fname = request.form.get("userinput")
    # if request.method == "POST" and fname:
#  my_files = open("userinput_datafile.txt", "w")
        # with open('userinput_datafile.txt', 'a') as f:
            # f.write(str(fname))
            
        # return render_template("userinput.html", userinputs=fname)
    # return render_template('indexkemalphones.html')

# my_files.close()

    

@app.route("/contactus")
def send():

    return render_template('contactus.html')

# @app.route('/alertuser', methods=('GET', 'POST'))
# def sendalert():
#     if request.method == 'POST':
#         data=[userinput, modele, Problems ]
#         userinput=request.form.get("fname")  
#         modele=request.form.get("modele")
#         Problems=request.form.get("problem")

#         if not userinput:
#             flash('fname is required!')
#             if not modele:
#                 flash('modele is required!')
#                 if not Problems:
#                     flash('problem is required!')
#         else:
#             conn = get_db_connection()
#             conn.execute('insert into userinput (fname, modele, problem, created ) values (?,?,?,datetime())', data)
#             conn.commit()
#             conn.close()
#             return redirect(url_for('indexkemalphones.html'))

#     return render_template('alertuser.html')

# def isalpha():
#     conn = get_db_connection()
#     userinputs = seeuser()

#     if request.method == 'POST':
#         session['userinput'] = request.form[('fname')]
#         ['userinput']  == ("fname")
#         userinput = "fname"
        
#         if ['userinput']  != ("fname").isalpha():
#             flash('Enter a correct first name!')
            
#             if ("fname").isalpha() == False:
#                 flash('Enter a correct first name!')
    

    #  conn.commit()

#     conn.close()
   
#     return isalpha([userinput.isalpha() for userinput in userinputs])
    # return userinput
    
# @app.route("/userinput", methods=["GET","POST"])
# def seeuser():
    # if request.method == 'POST':
    #     session['userinput'] = request.form[('fname')]
        # print (fname)
        # print(session['userinput'])
        # ['userinput']  == ("fname")
        
        # if ['userinput']  == ("fname").isalpha():
        #flash('Enter a correct first name!')
        # return render_template("androidapp.html")

    # return render_template('userinput.html')

# @app.route('/androidapp', methods=['GET', 'POST'])
# def searchmodel():
#     if request.method == "POST":
#         fname=request.form.get("fname")
#         session.pop('fname', None)
#         modele=request.form.get("modele")
#         session.pop('modele', None)
#         modeles=request.form.get("modeles")
#         session.pop('modeles', None)
#         Problems=request.form.get("Problems")
#         session.pop('problem', None)


#         session['userinput'] = fname
#         session['modele'] = modele
#         session['problem'] = Problems
#         store(session['userinput'],modele,Problems)
        
#     else:
#         return redirect(url_for(home_page()))

#     return render_template("androidapp.html")

# @app.route("/iOSapp", methods=['GET', 'POST'])
# def searchmodelmac():
#     if request.method == "POST":
#         fname=request.form.get("fname")
#         session.pop('fname', None)
#         modele=request.form.get("modele")
#         session.pop('modele', None)
#         modeles=request.form.get("modeles")
#         session.pop('modeles', None)
#         Problems=request.form.get("Problems")
#         session.pop('problem', None)

#         session['userinput'] = fname
#         session['modele'] = modele
#         session['problem'] = Problems

#         store(session['userinput'],modele,Problems)

#     else:

#         return render_template("iOSapp.html")
      

#     return render_template("indexkemalphones.html")


# def store(userinput,modele,problem):
#     conn = get_db_connection()
#     conn = sqlite3.connect('static/database.db')
#     cursor = conn.cursor()

#     data=[userinput, modele, problem ]

#     try:
#     # Insert a row with a non-null value for fname
#         conn.execute('insert into userinput(fname, modele, problem, created ) values (?,?,?,datetime())', data)
#     except sqlite3.IntegrityError as e:
        
#         conn.commit()
    
#     conn.close()
#     if userinput is None:
#         abort(404)

#     return userinput

# @app.route('/indexkemalphones', methods=["GET", "POST"])
# def liste():

#     conn = get_db_connection()
#     resultat = conn.execute('SELECT * FROM userinput').fetchall()
    
#     conn.commit()
    
#     conn.close()
#     return render_template('indexkemalphones.html', userinputs=resultat)

# def search_userinput():
#      conn = get_db_connection()
    
#      resultat = conn.execute('select * from userinput , sqlite_sequence where id = seq ').fetchall()
     
#      conn.commit()

#      conn.close()

#      return render_template('indexkemalphones.html', userinputs=resultat)

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


if __name__ == "__main__":
    app.run(debug=True)
