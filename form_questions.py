# -*- coding: utf-8 -*-

from flask import Flask, request, make_response, Response
import os
import json
import time
from slackclient import SlackClient
from init_data import *

def form_question(question_id):
    db = connect_to_mongo()
    question_dic = db.questions.find({"_id": question_id})
    actions = [{"name": question_dic["question"], "text": question_dic["question"], "value": question_dic["question"], "type": "button"} for x in question_dic["choices"]]
    attachments_json = [
        {
            "fallback": "您的肤质是...",
            "title": question,
            "color": "#3AA3E3",
            "attachment_type": "default",
            "callback_id": question_id,
            "actions": actions
        }
    ]