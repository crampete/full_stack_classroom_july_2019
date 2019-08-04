from flask import Flask, jsonify


app = Flask(__name__)


weather = {
    'chennai': {'temperature': 30, 'status': 'cloudly'},
    'mumbai': {'temperature': 25, 'status': 'raining'},
    'srinagar': {'temperature': -10, 'status': 'snow'},
    'madurai': {'temperature': 30, 'status': 'sunny'}
}


@app.route('/')
def home():
    return "Welcome to our weather service."


@app.route('/weather/<city_name>')
def city(city_name):
    return jsonify(weather[city_name])


app.run(debug=True)

# if __name__ == "__main__":
#     app.run()
