from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    with open("data.txt", "a") as f:
        f.write(str(request.form) + "\n")
    return "Processing..."

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
