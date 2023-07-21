# -*- coding: utf-8 -*-
"""
This script is to augment the AMZN customer review text and sentiment analysis
by comparing the difference between "good" words such as the difference between "like" and "love"
and the difference between "bad" and "good" words:  'junk' and 'quality'
for marketing purposes
"""
import pandas as pd
from scipy import stats

file_name = 'df_ID_Sentiments_keywords.csv'
control_word ='product great'
treatment_word = 'performs excellent'

# Read the CSV file or create a DataFrame from your data
#df = pd.read_csv('your_data.csv')  # Replace 'your_data.csv' with the actual file path
df = pd.read_csv('C:\\Users\\rober\\Downloads\\' + file_name)

# Split the data into control and treatment groups
control_group = df[df['keywords'].str.contains(control_word)]['Sentiment']
treatment_group = df[df['keywords'].str.contains(treatment_word)]['Sentiment']

# Perform a statistical test (e.g., t-test) to compare the groups
t_stat, p_value = stats.ttest_ind(control_group, treatment_group)

# Print the results
print("control group word: " + control_word + " treatment group word: " + treatment_word)
print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# Check for statistical significance based on the p-value
alpha = 0.05  # Set your desired significance level
if p_value < alpha:
    print("The difference between groups is statistically significant.")
else:
    print("The difference between groups is not statistically significant.")

