# app.py
import os
import sys
from flask import Flask, request, jsonify
app = Flask(__name__)

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '.'))
import datetime_service as ds

@app.route('/message', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    response = {}

    response["datetime"] = ds.get_datetime()
    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "Name is not specified"
        response["status_code"] = 400
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "Name cannot be number"
        response["status_code"] = 400
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = "Welcome " + name + " on this site!!"
        response["status_code"] = 200

    # Return the response in json format
    return jsonify(response)


@app.route('/')
def index():
    return "<h1>Welcome to Irtiza's server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, host="0.0.0.0", port=5000)
