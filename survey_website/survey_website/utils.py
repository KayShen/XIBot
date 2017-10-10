import os
import pandas as pd
from pyhive import presto
from datetime import datetime, timedelta

def connect_to_presto(query):
    con = presto.connect(host='10.115.1.81',
                      port='8080',
                      username='user_history', ## Change your name here so you can track your query on dashboard
                      catalog='hive')
    my_df = pd.read_sql(query, con)
    return(my_df)

# def get_user_history(client_id, year, month, day, lasting = 28):
#     client_id_lower = client_id.lower().replace("-", "")
#     last_date = datetime(year, month, day) + timedelta(days = lasting)
#     last_date_year = last_date.year
#     last_date_month = last_date.month
#     last_date_day = last_date.day
#     select_statement = "*"
#     where_statement = "where ((year = " + str(year) + " and month = " + str(month) + " and day <= 31 and day >= " + str(day) + \
#     ") or (year = "  + str(last_date_year) + " and month = " + str(last_date_month) + " and day >= 1 and day <= " + str(last_date_day) + "))"
#     user_history_query = "SELECT " + select_statement + " FROM hive.profx.user_history " + where_statement + " and client_id_top = '" + client_id_lower[0:2] + \
#     "' and client_id = '" + client_id_lower + "' order by ts"
#     return([x for x in connect_to_presto(user_history_query).to_dict(orient="index").values()])

def get_user_history(client_id, year, month, day, lasting = 28):
    return([x for x in pd.read_csv("/Users/ke.shen/Downloads/temp.csv").to_dict(orient="index").values()])
# # get_user_history("ee402fd0c87b40299c540ddfbd42bfbb", 2017, 4, 1)
