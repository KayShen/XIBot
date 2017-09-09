# -*- coding: utf-8 -*-

from flask import Flask, request, make_response, Response
import os
import json
import time
from slackclient import SlackClient
from form_questions import *

slack_client = SlackClient('xoxb-232306006676-UbSba54K94umFZYRuDFtZDCo')

app = Flask(__name__)

@app.route("/response", methods=["POST"])
def message_options():
    form_json = json.loads(request.form["payload"])
    print(form_json)

    attachments_json = form_questions("001001")
    
    slack_client.api_call(
      "chat.postMessage",
      channel=form_json["channel"]["id"],
      text="你是痘痘肌吗？",
      attachments=attachments_json
    )

    # return Response(json.dumps(menu_options), mimetype='application/json')
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3500)