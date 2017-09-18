# -*- coding: utf-8 -*-

from flask import Flask, request, make_response, Response
import os
import json
import time
from slackclient import SlackClient
from init_data import *

def form_question(question_id):
    db = connect_to_mongo()
    question_dic = db.questions.find_one({"_id": question_id})
    actions = [{"name": v, "text": v, "value": k, "type": "button"} for k, v in question_dic["choices"].items()]
    attachments_json = [
        {
            "fallback": question_dic["question"],
            "title": question_dic["question"],
            "color": "#3AA3E3",
            "attachment_type": "default",
            "callback_id": question_id,
            "actions": actions
        }
    ]
    return attachments_json

def get_next_question(question_id):
    db = connect_to_mongo()
    return db.next_question.find_one({"_id": question_id})["next_question_id"]
# form_question("000001")
