from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from functools import wraps
import os
from DbClass import DbClass
import distanceCalculator

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
                g.user = user_credentials[0]
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
    #gebruikersnaam = session.get('username', None)
    return render_template("statistics.html") #gebruikersnaam = gebruikersnaam)

@app.route('/sessions')
def sessions():
    db = DbClass()
    sessionList = db.getSessions()
    return render_template("sessions.html", sessionList=sessionList)

@app.route('/sessiondetail/<sessionID>')
def sessiondetail(sessionID):
    db = DbClass()
    coordinates = db.getCoordinates(sessionID)
    speedAndTime = db.getSpeedAndTime(sessionID)
    totaleAfstand = distanceCalculator.afstandBerekenen(coordinates)
    return render_template("sessiondetail.html", sessionID=sessionID, coordinates=coordinates, speedAndTime=speedAndTime, totaleAfstand=totaleAfstand)

# -----------------------------------------------------------

@app.route('/weekly-overview')
def weeklyoverview():
    db = DbClass()
    totalSessions = db.getWeekSessionCount()
    totalTime = db.getWeekTotalTime()
    averageTime = db.getWeekAverageTime()
    topSpeed = db.getWeekTopSpeed()
    averageSpeed = db.getWeekAverageSpeed()
    highestAltitude = db.getWeekHighestAltitude()
    lowestAltitude = db.getWeekLowestAltitude()
    altitudeDifference = db.getWeekAltitudeDifference()
    return render_template("weeklyoverview.html", totalSessions=totalSessions, totalTime=totalTime, averageTime=averageTime, topSpeed=topSpeed, averageSpeed=averageSpeed, highestAltitude=highestAltitude, lowestAltitude=lowestAltitude, altitudeDifference=altitudeDifference)

# -----------------------------------------------------------
@app.route('/total')
def total():
    db = DbClass()
    totalSessions = db.getTotalSessionCount()
    totalTime = db.getTotalTotalTime()
    averageTime = db.getTotalAverageTime()
    topSpeed = db.getTotalTopSpeed()
    averageSpeed = db.getTotalAverageSpeed()
    highestAltitude = db.getTotalHighestAltitude()
    lowestAltitude = db.getTotalLowestAltitude()
    altitudeDifference = db.getTotalAltitudeDifference()
    return render_template("total.html", totalSessions=totalSessions, totalTime=totalTime, averageTime=averageTime, topSpeed=topSpeed, averageSpeed=averageSpeed, highestAltitude=highestAltitude, lowestAltitude=lowestAltitude, altitudeDifference=altitudeDifference)

@app.route('/test')
def test():
    return render_template("test.html")

if __name__ == '__main__':
    #flask op pc:
    #app.run

    #flask op pi:
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000, debug=True)