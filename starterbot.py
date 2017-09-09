import os
import time
from slackclient import SlackClient


# starterbot's ID as an environment variable
# BOT_ID = os.environ.get("BOT_ID")
BOT_ID = "U6U9006KW"
# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

# instantiate Slack & Twilio clients
# slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
slack_client = SlackClient('xoxb-232306006676-UbSba54K94umFZYRuDFtZDCo')

attachments_json = [
    {
        "fallback": "您的肤质是...",
        "title": "您的肤质是...",
        "color": "#3AA3E3",
        "attachment_type": "default",
        "callback_id": "question_1",
        "actions": [
            {   
                "name": "干皮",
                "text": "干皮",
                "value": "干皮",
                "type": "button",
            },
            {
                "name": "混合偏干",
                "text": "混合偏干",
                "value": "混合偏干",
                "type": "button",
            },
            {
                "name": "混合",
                "text": "混合",
                "value": "混合",
                "type": "button",
            },
            {
                "name": "混合偏油",
                "text": "混合偏油",
                "value": "混合偏油",
                "type": "button",
            },
            {
                "name": "油皮",
                "text": "油皮",
                "value": "油皮",
                "type": "button",
            },
            {
                "name": "不太确定",
                "text": "不太确定",
                "value": "不太确定",
                "type": "button",
            }
        ]
    }
]

def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."
    if command == 'start':
        slack_client.api_call(
          "chat.postMessage",
          channel=channel,
          text="您的肤质是？",
          attachments=attachments_json
        )

    elif command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!"
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)




def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 0 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
