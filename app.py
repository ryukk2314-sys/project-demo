from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get("name")
    mobile = request.form.get("mobile")
    village = request.form.get("village")
    mpin = request.form.get("mpin")
    pincode = request.form.get("pincode")

    # ✅ Validation (sab fill hona chahiye)
    if not name or not mobile or not village or not mpin or not pincode:
        return "Please fill all fields"

    # ✅ Data save
    with open("data.txt", "a") as f:
        f.write(f"{name}, {mobile}, {village}, {mpin}, {pincode}\n")

    return "Submitted successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
