from flask import Blueprint, render_template, session, flash, redirect, url_for, request

auth = Blueprint("auth", __name__)

# @auth.route("/register", methods=["POST", "GET"])
# def register():
#   if request.method == "POST":
#     # session.permanent=True
    
#     name = request.form.get("name")
#     email = request.form.get("email")
#     password = request.form.get("password")
    
#     # print(name, email, password)
    
#     session["name"] = name
#     session["email"] = email
#     session["password"] = password
    
#     # old_user = users.query.filter_by(email = email).first()
    
#     # if old_user:
#     #   session["email"] = old_user.email
#     # else:
#     #   name = session["name"]
#     #   email = session["email"]
#     #   password = session["password"]
      
#     #   new_user = users(name=name, email=email, password=password)
#     #   db.session.add(new_user)
#     #   db.session.commit()
    
#     return redirect(url_for("home"))
  
#   return render_template("register.html")

@auth.route("/login", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    session.permanent = True
    
    password = request.form.get("password")
    email = request.form.get("email")
    name = request.form.get("name")

    session["name"] = name
    session["email"] = email 
    session["password"] = password

    return redirect(url_for("home"))
  else:
    if "name" in session:
      flash("Already logged in!")
      return redirect(url_for("home"))
    
    return render_template("login.html")


@auth.route("/logout")
def logout():
  if "name" and "email" in session:
    session.pop("name", None)
    session.pop("email", None)
    flash("You have been logged out!", "info")
  return redirect(url_for("auth.login"))