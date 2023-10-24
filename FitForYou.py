from flask import Flask, flash, redirect, url_for, render_template, session
from flask import request
from datetime import datetime
from itertools import cycle

from flask_sqlalchemy import SQLAlchemy


DB_HOST = "localhost"
DB_NAME = "FitDB"
DB_USERNAME = "root"
DB_Password = "MotorcycleNoises23!"

database_file = f"mysql+pymysql://{DB_USERNAME}:{DB_Password}@{DB_HOST}:3306/{DB_NAME}"

app = Flask(__name__)
app.secret_key = "mysecret"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    userpass = db.Column(db.String(100), nullable=False)

    def __init__(self, username, userpass):
        self.username = username
        self.userpass = userpass

class workout_tracker(db.Model):
    __tablename__ = 'workout_tracker'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    workout_date = db.Column(db.Date, nullable=False)
    workout = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Integer, nullable=False)

    def __init__(self, username, workout_date, workout, calories):
        self.username = username
        self.workout_date = workout_date
        self.workout = workout
        self.calories = calories

class meal_tracker(db.Model):
    __tablename__ = 'meal_tracker'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    meal_date = db.Column(db.Date, nullable=False)
    meal = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Integer, nullable=False)

    def __init__(self, username, meal_date, meal, calories):
        self.username = username
        self.meal_date = meal_date
        self.meal = meal
        self.calories = calories

@app.route("/")
def home():
    todayDate = datetime.today().strftime('%Y-%m-%d')

    if 'currentUser' in session:
        username = session['currentUser']

        #trying to set username so we can change the sign in button on the html page (this can be changed)
        return render_template("home.html", todayDate = todayDate, username=username)
    return render_template("home.html", todayDate = todayDate)

@app.route("/signout")
def signout():
    session['isSignedIn'] = False
    session['currentUser'] = ""
    return redirect(url_for('home'))

@app.route("/users")
def users():
    return render_template("userList.html", users=User.query.all())

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == 'POST':
        if not request.form['username'] or not request.form['userpass']:
            flash('Please enter all the fields', 'error')
        else:
            user = User(request.form['username'], request.form['userpass'])

            db.session.add(user)
            db.session.commit()

            flash('Record was successfully added')
            return redirect(url_for('signin'))
    return render_template("signup.html")

@app.route("/signin", methods = ["GET", "POST"])
def signin():
    if request.method == 'POST':
            if not request.form['username'] or not request.form['userpass']:
                flash('Please enter all the fields', 'error')
            else:
                if bool(db.session.query(User).filter_by(username=request.form['username']).first()) and bool(db.session.query(User).filter_by(userpass=request.form['userpass']).first()):
                   #setting session varaible for username
                    session['currentUser'] = request.form['username']
                    session['isSignedIn'] = True
                    flash('Record was successfully added')
                    return redirect(url_for('home'))
                else:
                    flash('User does not exist', 'error')
    return render_template("signin.html")

@app.route("/tracker")
def tracker():
    return render_template("workout_tracker.html", workout_tracker=workout_tracker.query.all())


@app.route('/add_workout/<date>', methods=['GET', 'POST'])
def add_work(date):
    if request.method == 'POST':
        if not request.form['workout'] or not request.form['calories']:
            flash('Please enter all the fields', 'error')
        else:
            tracker = workout_tracker(session['currentUser'], date, request.form['workout'], request.form['calories'])

            db.session.add(tracker)
            db.session.commit()

            flash('Record was successfully added')
            return redirect(url_for('info', date = date))
    return render_template('add_workout.html', date = date)

@app.route('/delete_work/<int:id>/<date>', methods=['GET', 'POST'])
def delete_work(id, date):
    if request.method == 'POST':
        tracker = workout_tracker.query.filter_by(id=id).first()
        db.session.delete(tracker)
        db.session.commit()

        flash('Record was successfully deleted')
        return redirect(url_for('info', date=date))
    data = workout_tracker.query.filter_by(id=id).first()
    return render_template("delete_work.html", data=data, date = date)

@app.route('/add_meal/<date>', methods=['GET', 'POST'])
def add_meal(date):
    if request.method == 'POST':
        if not request.form['meal'] or not request.form['calories']:
            flash('Please enter all the fields', 'error')
        else:
            mtracker = meal_tracker(session['currentUser'], date, request.form['meal'], request.form['calories'])

            db.session.add(mtracker)
            db.session.commit()

            flash('Record was successfully added')
            return redirect(url_for('info', date = date))
    return render_template('add_meal.html', date = date)


@app.route('/delete_meal/<int:id>/<date>', methods=['GET', 'POST'])
def delete_meal(id, date):
    if request.method == 'POST':
        mtracker = meal_tracker.query.filter_by(id=id).first()
        db.session.delete(mtracker)
        db.session.commit()

        flash('Record was successfully deleted')
        return redirect(url_for('info', date=date))
    data = meal_tracker.query.filter_by(id=id).first()
    return render_template("delete_meal.html", data=data, date = date)

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/info/<date>", methods=['GET', 'POST'])
def info(date):
    fitInfo = zip(workout_tracker.query.filter_by(username=session["currentUser"], workout_date=date), cycle(meal_tracker.query.filter_by(username=session["currentUser"], meal_date=date))) if workout_tracker.query.filter_by(username=session["currentUser"], workout_date=date).count() > meal_tracker.query.filter_by(username=session["currentUser"], meal_date=date).count() else zip(cycle(workout_tracker.query.filter_by(username=session["currentUser"], workout_date=date)), meal_tracker.query.filter_by(username=session["currentUser"], meal_date=date))
    altFit = zip(workout_tracker.query.filter_by(username=session["currentUser"], workout_date=date), cycle(meal_tracker.query.filter_by(username=session["currentUser"], meal_date=date))) if workout_tracker.query.filter_by(username=session["currentUser"], workout_date=date).count() > meal_tracker.query.filter_by(username=session["currentUser"], meal_date=date).count() else zip(cycle(workout_tracker.query.filter_by(username=session["currentUser"], workout_date=date)), meal_tracker.query.filter_by(username=session["currentUser"], meal_date=date))
    return render_template("viewinfo.html", myDate=date, fitInfo = fitInfo, curUser = session["currentUser"], fullW=workout_tracker.query.filter_by(username=session["currentUser"], workout_date=date), fullM = meal_tracker.query.filter_by(username=session["currentUser"], meal_date=date), zipList = list(altFit))

@app.context_processor
def utility_functions():
    def print_in_console(message):
        print (message)

    return dict(mdebug=print_in_console)


@app.route("/fittracker")
def fit_tracker():
    return render_template("fitness_tracker.html")

