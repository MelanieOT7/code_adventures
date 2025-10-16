from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from models.db import init_db
import models.user as user_logic
import models.account as account_logic

app = Flask(__name__)
app.secret_key = "supersecretkey"
init_db()

@app.route("/")
def home():
    return redirect(url_for("login"))

# Login page
@app.route("/login")
def login():
    return render_template("login.html")

# Signup
@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    success, message = user_logic.create_user(data["username"], data["password"])
    return jsonify({"status": "success" if success else "error", "message": message})

# Login verify
@app.route("/login_verify", methods=["POST"])
def login_verify():
    data = request.json
    success, info = user_logic.verify_user(data["username"], data["password"])
    if success:
        session["user_id"] = info
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": info})

# Dashboard
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html")

# Logout
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("login"))

# Account, transaction APIs (update to use session["user_id"])...
# For example:
@app.route("/accounts", methods=["GET"])
def accounts():
    user_id = session.get("user_id")
    return jsonify(account_logic.get_accounts(user_id))
