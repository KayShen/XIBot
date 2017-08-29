import pymongo
from pymongo import MongoClient
import pandas as pd
import sys
import os

def connect_to_mongo(mongodb_ip = '52.220.88.110'):
    url = "mongodb://xiuser:Xiaoxi@"+ mongodb_ip +"/xigroup"
    client = MongoClient(url)
    db = client.xigroup
    return db

def insert_data(datapath = "data/makeup.txt"):
	xl = pd.ExcelFile("data/makeup.xlsx")
	df = xl.parse("Sheet1")
	return df