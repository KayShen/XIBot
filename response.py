# -*- coding: utf-8 -*-

from flask import Flask, request, make_response, Response
import os
import json
import time
from slackclient import SlackClient
from form_questions import *

slack_client = SlackClient('xoxb-232306006676-PgGkz7iziRxDQidfuZMlXKNa')

app = Flask(__name__)

@app.route("/response", methods=["POST", "GET"])
def message_options():
    form_json = json.loads(request.form["payload"])
    print(form_json)
    previous_question_id = form_json['callback_id']
    attachments_json = form_question("001001")

    slack_client.api_call(
      "chat.postMessage",
      channel=form_json["channel"]["id"],
      attachments=attachments_json
    )

    return ""
    # return Response(json.dumps(menu_options), mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3500)
