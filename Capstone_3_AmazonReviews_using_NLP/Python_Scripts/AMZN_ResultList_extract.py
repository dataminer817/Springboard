#  
# -*- coding: utf-8 -*-
"""
This script extracts Review column info in the original CSV file into a separate table: a separate table is needed because the original Review 
column is a list data structure with many embedded dictionaries in the list of Review column data.
Further comments below when explanation is needed:
"""
#
import ast
import pandas as pd

file_name = 'Aug31ReviewList.csv'
lab_df = pd.read_csv('C:\\Users\\rober\\OneDrive\\DS_Springboard\\Unit_30\\Amazon_Reviews_I\\' + file_name)
REVIEWLIST_df = pd.DataFrame()

# Iterating over each row in the DataFrame, not just the 'RESULTLIST' column
for idx, row in lab_df.iterrows():
    # Converting the string to a list of dictionaries
    try:
        list_of_dicts = ast.literal_eval(row['REVIEWLIST'])
    except SyntaxError:
        continue
    
    # Iterating over each dictionary in the list
    for dictionary in list_of_dicts:
        for k, v in dictionary.items():
            try:
                print(f'ID: {row["ID"]}, {k}: {v}')
                REVIEWLIST_df = REVIEWLIST_df.append({'ID': row["ID"], 'key': k,'value': v},ignore_index=True)
            except SyntaxError:
                continue
            
print(REVIEWLIST_df.head())

test_file_name = 'view_reviewlist_column.csv' 
REVIEWLIST_df.to_csv('C:\\Users\\rober\\OneDrive\\DS_Springboard\\Unit_30\\Amazon_Reviews_I\\' + test_file_name, index=False)