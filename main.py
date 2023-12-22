from flask import Flask, render_template, flash, request, redirect, sessions, url_for, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String

from flask_sqlalchemy import SQLAlchemy
from auth import auth as auth_blueprint

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)
app.secret_key = "munyi"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=30)
db.init_app(app)

app.register_blueprint(auth_blueprint)

class User(db.Model):
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
  email: Mapped[str] = mapped_column(String)
  password: Mapped[str] = mapped_column(String)
  
with app.app_context():
  db.create_all()
  
# class Users(db.Model):
#   id  = db.Column(db.Integer, primary_key = True)
#   name = db.Column(db.String(100), nullable=False)
#   email = db.Column(db.String(100), nullable=False, unique = True)
#   password = db.Column(db.String(50))
  
#   def __init__(self, name, email, password):
#     self.name = name
#     self.email = email
#     self.password = password

@app.route("/")
def home():
  if "name" and "email" in session:
    email = session["email"]
    name = session["name"]
    
    flash("Logged in successfully!")
    return render_template("home.html", name = name, email = email)
  else:
    flash("You need to be logged in first to access this page.")
    return redirect(url_for("auth.login"))  

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/register", methods=["POST", "GET"])
def register():
  if request.method == "POST":
    # session.permanent=True
    
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    
    new_user = User(name = name, email  = email, password = password) # type: ignore
            
    db.session.add(new_user)
    db.session.commit()
    
    print(name, email, password)
    
    # session["name"] = name
    # session["email"] = email
    # session["password"] = password
    
    old_user = User.query.filter_by(email=email).first()
    
    if old_user:
      flash("User with the same email already exists")
      return redirect(url_for("register"))
    else:
      # name = session["name"]
      # email = session["email"]
      # password = session["password"
          
      return redirect(url_for("home"))
  
  return render_template("register.html")

if __name__ == "__main__":
  app.run(debug=True)