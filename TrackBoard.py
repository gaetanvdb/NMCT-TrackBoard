from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps
import os
from DbClass import DbClass

app = Flask(__name__)
app.secret_key = "y0SP04}7K.:rbB+)9-&m:cl/j<o7j_sPG#vV?yL(i7HYx[53Y!}WW<oy`DA,p!Z"


#Login vereist def
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for("login"))
    return wrap




# PAGINA's
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():

    error = None
    if request.method == "POST":
        db = DbClass()
        user_credentials = db.getUser(request.form['username'])
        print(user_credentials)
        if user_credentials: #Als de lijst NIET leeg is dan...
            if (user_credentials[1]) != request.form['password']:
                error = 'invalid credentials. Please try again.'
            else:
                session['logged_in'] = True
                session['username'] = user_credentials[0]
                flash('you were just logged in!')
                return redirect(url_for("statistics"))
        else:
            error = 'invalid credentials. Please try again.'
    return render_template("login.html", error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('you were just logged out!')
    return redirect(url_for("index"))

@app.route('/statistics')
@login_required
def statistics():
    gebruikersnaam = session.get('username', None)
    return render_template("statistics.html", gebruikersnaam = gebruikersnaam)

@app.route('/sessions')
def sessions():
    return render_template("sessions.html")

@app.route('/sessiondetail/<sessionID>')
def sessiondetail(sessionID):
    return render_template("sessiondetail.html")

@app.route('/weekly-overview')
def weeklyoverview():
    return render_template("weeklyoverview.html")

@app.route('/total')
def total():
    return render_template("total.html")


if __name__ == '__main__':
    #flask op pc:
    #app.run

    #flask op pi:
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000, debug=True)
