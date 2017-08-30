from flask import Flask, request, make_response, Response
import os
import json

app = Flask(__name__)

@app.route("/response", methods=["POST"])
def message_options():
	form_json = json.loads(request.form["payload"])
	print form_json

if __name__ == "__main__":
    run(host='0.0.0.0', port=3500, debug=True)