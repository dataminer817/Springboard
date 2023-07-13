# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 14:07:05 2023

@author: rober
"""
import pandas as pd  
import numpy as np

#
file_name = 'df_categories.csv'
df_categories = pd.read_csv('C:\\Users\\rober\\Downloads\\' + file_name)

df2 = pd.DataFrame(columns=['ID','Sentiment','keywords'])
for i in range(len(df_categories)):
    for word in df_categories['keywords'][i].split():
        df2 = df2.append({'ID': df_categories['ID'][i], 
                            'Sentiment': df_categories['Sentiment'][i], 
                            'keywords': word}, ignore_index=True)
print(df2)

test_file_name = 'category_keyword_list.csv' 
df2.to_csv('C:\\Users\\rober\\Downloads\\' + test_file_name, index=False)
