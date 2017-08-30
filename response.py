from flask import Flask, request, make_response, Response
import os
import json
import time
from slackclient import SlackClient

# slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

app = Flask(__name__)

@app.route("/response", methods=["POST"])
def message_options():
    form_json = json.loads(request.form["payload"])

    menu_options = {
        "options": [
            {
                "text": "Chess",
                "value": "chess"
            },
            {
                "text": "Global Thermonuclear War",
                "value": "war"
            }
        ]
    }

    return Response(json.dumps(menu_options), mimetype='application/json')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3500)