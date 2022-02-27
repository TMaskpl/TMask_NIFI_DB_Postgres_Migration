#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import sys

destination_table_schema = sys.argv[1]
destination_table_name = sys.argv[2]

s_json = sys.stdin.read()
dict = json.loads(s_json)

# Mapping
# my_dictionary = {
#     'integer':'int', 
#     'character varying':'varchar'    
#     }

c_name = []
d_type = []

for d in dict:
    c_name.append(d['column_name'])
    d_type.append(d['data_type'])

sql_query = f'CREATE SCHEMA IF NOT EXISTS {destination_table_schema};\n'
sql_query += f"CREATE TABLE {destination_table_schema}.{destination_table_name}(\n"

for column, datatype in zip(c_name, d_type):
    sql_query += f"\t{column} {datatype},\n"

sql_query += ");"
sql = sql_query.replace(",\n);", ");")

print(sql)
