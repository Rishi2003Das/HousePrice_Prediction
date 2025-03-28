import json
import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, url_for, session

# Add this at the start of your app.py for more detailed error tracking
import traceback
import sys

try:
    import numpy as np
    print("NumPy Version:", np.__version__)
except Exception as e:
    print("Detailed NumPy Import Error:")
    traceback.print_exc()
    sys.exit(1)

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Secret key for session management

# Load the model and scaler
regmodel = pickle.load(open('regmodel.pkl', 'rb'), encoding='latin1')
scalar = pickle.load(open('scaling.pkl', 'rb'))

# Hardcoded login credentials (for demo purposes)
USERNAME = "admin"
PASSWORD = "password123"


# 🔹 Login Page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            session["user"] = username  # Store user session
            return redirect(url_for("home"))  # Redirect to home page
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


# 🔹 Home Page (Protected)
@app.route("/home")
def home():
    if "user" not in session:
        return redirect(url_for("login"))  # Redirect to login if not authenticated
    return render_template("home.html")


# 🔹 Predict API (POST Request for JSON Data)
@app.route("/predict_api", methods=["POST"])
def predict_api():
    if "user" not in session:
        return jsonify({"error": "Unauthorized access"}), 403  # Restrict API access if not logged in

    data = request.json["data"]
    new_data = scalar.transform(np.array(list(data.values())).reshape(1, -1))
    output = regmodel.predict(new_data)
    return jsonify(output[0])


# 🔹 Predict Function (For Web Form Submission)
@app.route("/predict", methods=["POST"])
def predict():
    if "user" not in session:
        return redirect(url_for("login"))  # Ensure only logged-in users can predict

    data = [float(x) for x in request.form.values()]
    final_input = scalar.transform(np.array(data).reshape(1, -1))
    print(final_input)
    output = regmodel.predict(final_input)[0]
    return render_template("home.html", prediction_text=f"The House price prediction is {output}")


# 🔹 Logout Function
@app.route("/logout")
def logout():
    session.pop("user", None)  # Remove user session
    return redirect(url_for("login"))  # Redirect to login page


if __name__ == "__main__":
    app.run(debug=True)
