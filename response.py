from flask import Flask, request, make_response, Response
import os
import json
import time
from slackclient import SlackClient

slack_client = 'xoxb-232306006676-RbKxztSArd46oopnAJFlE2Bn'

app = Flask(__name__)

attachments_json = [
    {
        "fallback": "你是痘痘肌吗？...",
        "title": "你是痘痘肌吗？...",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "question_2",
        "actions": [
            {   
                "name": "1",
                "text": "是痘痘肌，想用对痘痘肌肤友好的产品",
                "value": "1",
                "type": "button",
            },
            {
                "name": "2",
                "text": "有痘印，想用遮瑕度高的产品",
                "value": "2",
                "type": "button",
            },
            {
                "name": "3",
                "text": "没有痘痘困扰",
                "value": "3",
                "type": "button",
            }
        ]
    }
]


@app.route("/response", methods=["POST"])
def message_options():
    form_json = json.loads(request.form["payload"])
    print(form_json)
    slack_client.api_call(
      "chat.postMessage",
      channel=channel,
      text="你是痘痘肌吗？",
      attachments=attachments_json
    )

    # return Response(json.dumps(menu_options), mimetype='application/json')
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3500)