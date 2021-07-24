from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['POST'])
def blue_coop():
    blue_req = request.json
    print("Message from blue pigeon received")
    print(blue_req)
    return "Thank you, message received\n"