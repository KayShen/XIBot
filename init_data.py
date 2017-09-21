import pymongo
from pymongo import MongoClient
import pandas as pd
import sys
import os
import json

def connect_to_mongo(mongodb_ip = ''):
    url = "mongodb://@"+ mongodb_ip +"/"
    client = MongoClient(url)
    db = client.xigroup
    return db

def insert_makeup_data(datapath = "data/makeup.txt"):
    xl = pd.ExcelFile("data/makeup.xlsx")
    df = xl.parse("Sheet1")
    data_dict = df.to_dict(orient="index")
    db = connect_to_mongo()
    db.makeups.insert_many(data_dict.values())

def insert_question_data(datapath = "data/questions.json"):
    with open(datapath) as data_file:
        data = json.load(data_file)
    db = connect_to_mongo()
    db.questions.insert_many(data)

def insert_next_question_data(datapath = "data/next_question.json"):
    with open(datapath) as data_file:
        data = json.load(data_file)
    db = connect_to_mongo()
    db.next_question.insert_many(data)
