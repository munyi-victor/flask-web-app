from flask import Flask, render_template, flash, request, redirect, sessions, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "munyi"
app.permanent_session_lifetime = timedelta(minutes=30)

@app.route("/login", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    session.permanent=True
    name = request.form["name"]
    email = request.form["email"]
    
    session["name"] = name
    session["email"] = email

    return redirect(url_for("home"))
  else:
    if "name" in session:
      flash("Already logged in!")
      return redirect(url_for("home"))
    
    return render_template("login.html")

# @app.route("/user")
# def user():
#   if "name" and "email" in session:
#     name = session["name"]
#     email = session["email"]
    
#     return f"<h1>{name}</h1>"
#   else:
#     return redirect(url_for("login"))

@app.route("/logout")
def logout():
  if "name" and "email" in session:
    session.pop("name", None)
    session.pop("email", None)
    flash("You have been logged out!", "info")
  return redirect(url_for("login"))

@app.route("/")
def home():
  if "name" and "email" in session:
    name = session["name"]
    email = session["email"]
    
    flash("Logged in successfully!")
    return render_template("home.html", name=name, email=email)
  else:
    flash("You need to be logged in first to access this page.")
    return redirect(url_for("login"))

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

if __name__ == "__main__":
  app.run(debug=True)