from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hi"


@app.route('get_location_names')
def get_location_names():
    response = jsonify({
        'locations' : util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods = ['POST'])
def predict_home_price():
    total_sqft = float(request.form['toatl_sqft'])
    location = request.form['location']
    rooms = int(request.form['rooms'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price' : util.predict_price(location,total_sqft,rooms,bath)

    })
    return response

if __name__ == "__main__":
    print("strt")
    app.run()