import csv
import json
import pandas as pd
import math

file_count = 1
count = 0

df = pd.read_csv('./csv/amazon.csv')
jsonfile_base = './json_data/file_'

length = len(df)
rowcount = 50
runtime = math.ceil(length / rowcount)

for i in range(runtime):
    start_index = i * rowcount
    end_index = min((i + 1) * rowcount, length)
    fifty_values = df[start_index:end_index]
    fifty_values_dict = fifty_values.to_dict('records')
    print(fifty_values_dict)
    jsonfile = f'{jsonfile_base}{i + 1}.json'
    with open(jsonfile, 'w') as json_file_object:
        json.dump(fifty_values_dict, json_file_object, indent=2)
with open("json_data/file_1.json",'w') as new_line:
    ouput = new_line.replace(',','/n')