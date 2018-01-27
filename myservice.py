from flask import Flask
from flask import request
from flask import abort
from flask import jsonify

from validator import Validator
from thing import Thing

app = Flask(__name__)

# A function used for each API call that requires authentication.
def create_validator():
    try:
        v = Validator(request.headers.get('x-auth-token'))
    except:
        abort(403)
    return v


# Routes below.  The /-route can be used as a liveliness and ready probe.
@app.route("/")
def check():
    return jsonify({"myservice": 0.1})

@app.route("/v1/thing/list")
def thing_list():
    return jsonify(Thing(create_validator()).list_things())
