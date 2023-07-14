# -*- coding: utf-8 -*-
"""
This script takes df_categories.csv and creates a new table of 650,000 records:  ID, Sentiment, Keyword to view counts and types of keywords  
across various products, categories and their Sentiment scores.  The keywords is parsed or split out from the other CSV table that has a string Keywords 
which are larger blocks of text extracted from the original "Review" column info.
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
