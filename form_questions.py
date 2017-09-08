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