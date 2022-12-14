from flask import Flask,jsonify,request
from Project125 import getPrediction

app = Flask(__name__)

@app.route("/predictDigit",methods=["POST"])
def predictData():
    image = request.files.get("alphabet")
    prediction = getPrediction(image)   
    return jsonify({
        "prediction":prediction
    }),200

if(__name__ == "__main__"):
    app.run(debug=True)