from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "البوت شغال تمام!"

@app.route("/save")
def save():
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    print(f"Location: {lat}, {lon}")
    return f"تم استلام الموقع: {lat}, {lon}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
