# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 08:37:02 2023

@author: Robert
"""
#Code task 1#
#Import pandas, matplotlib.pyplot, and seaborn in the correct lines below
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#import datetime as dt
#import os

#from library.sb_utils import save_file   # ModuleNotFoundError: No module named 'library'

# the supplied CSV data file is the raw_data directory
credit_classify_test = pd.read_csv('C:\\Users\\\Robert\\.spyder-py3\\raw_data\\credit_classify_test.csv')

#Code task 2#
#Call the info method on credit_classify_test to see a summary of the data
credit_classify_test.info()
#print(credit_classify_test.head(20))

df=credit_classify_test
print('null_or_missing_checks:\n')
print(df.isnull().sum())
print('type_check: ',type(df), type(credit_classify_test))

#sns.boxplot(x=df['Name'])

#sns.displot(data=df['Type_of_Loan'])
print('dupe:\n')
print(df.duplicated().sum())
print('dupe_name:\n')
print(df['Name'].value_counts())

# Check for missing values
missing_values = df.isna().sum()
print('missing_values:\n')
print(missing_values)
# Calculate occupation spend patterns  and sort by the average of the two
# Hint: use the pattern dataframe.groupby(<grouping variable>)[<list of columns>].mean()
#occupation_amount_means = credit_classify_test.groupby(by='Occupation')[['Annual_Income', 'Outstanding_Debt']].mean()
#print(occupation_amount_means.head())

#outlier detection
print('outlier detection:')
print(df.describe([x*.1 for x in range(10) ]))

#extract duplicates
df_dupe=[df.duplicated()]
print(df_dupe)

# check if there are duplicates
print('df.duplicated().sum()')
print(df.duplicated().sum())

# Standardize SSN column to 'XXX-XX-XXXX'
df['SSN'] = df['SSN'].apply(lambda x: '-'.join(x.split(' ')[:3]))

# Drop the Age value in cell if it is not numeric
df = df[pd.to_numeric(df['Age'], errors='coerce').notnull()]

# Drop the Annual_Income value in cell if it is not numeric
df = df[pd.to_numeric(df['Annual_Income'], errors='coerce').notnull()]

# Drop the Monthly_Inhand_Salary value in cell if it is not numeric
df = df[pd.to_numeric(df['Monthly_Inhand_Salary'], errors='coerce').notnull()]



print(df[['Name','SSN', 'Age', 'Annual_Income', 'Monthly_Inhand_Salary' ]])

print(df.head(50))
#print(df[['Name','SSN', 'Age', 'Annual_Income', 'Monthly_Inhand_Salary', 'Num_Bank_Accounts', 'Num_Credit_Card', 'Interest_Rate','Num_of_Loan','Type_of_Loan' ]])
#print([df])



# Convert Age column to int
df['Age'] = df['Age'].apply(pd.to_numeric, errors='coerce')

# Create a new column fn_Age and assign value to it
df['fn_Age'] = df['Age'].apply(lambda x: x if (x >= 12 and x <= 99) else 'NaN')
#df2 = df['fn_Age']
#df2.to_csv('C:\\Users\\\Robert\\.spyder-py3\\raw_data\\cc_classify_out_test.csv')
# Display output of new column
print(df['fn_Age'])

# check interest rate
def fn_IRate(row):
    if row['Interest_Rate'] > 50:
        return 14.56 #np.mean(df['Interest_Rate'])
    else:
        return row['Interest_Rate']

df['fn_IRate'] = df.apply(fn_IRate, axis=1)

# Check for missing or null values in Num_of_Delayed_Payment column 
if df['Num_of_Delayed_Payment'].isnull().any(): 
  # Replace missing or null values with "NA"
  df['Num_of_Delayed_Payment'].fillna(".01", inplace = True) 


# Iterate thru the Num_of_Loan rows of the DF replace "_"
for i, row in df.iterrows():
    # If the row contains a '_', replace it with a zero length string
    if "_" in row["Num_of_Loan"]:
        df.loc[i,"Num_of_Loan"] = df.loc[i,"Num_of_Loan"].strip("_")
    if float(row["Num_of_Loan"].strip("_")) > 10:
        df.loc[i,"Num_of_Loan"] = 3.63  #df['Num_of_Loan'].mean()
    if float(row["Num_of_Loan"].strip("_")) <0:
            df.loc[i,"Num_of_Loan"] = 1.22  #df['Num_of_Loan'].mean()

   # Clean Num_of_Delayed_Payment
for i, row in df.iterrows():   
    if "_" in row["Num_of_Delayed_Payment"]:
        df.loc[i,"Num_of_Delayed_Payment"] = df.loc[i,"Num_of_Delayed_Payment"].strip("_")        
    if float(row["Num_of_Delayed_Payment"].strip("_")) > 50:    
        df.loc[i,"Num_of_Delayed_Payment"] = 22.01 #df['Num_of_Delayed_Payment'].mean()
    # replace neg val from Delay_from_due_date     
    if row["Delay_from_due_date"] <0:
                df.loc[i,"Delay_from_due_date"] = 0    
            
# Check for missing or null values in Type_of_Loan column 
if df['Type_of_Loan'].isnull().any(): 
  # Replace missing or null values with "NA"
  df['Type_of_Loan'].fillna("NA", inplace = True) 

# fn extract loan type info
def get_Auto_Loan_count(row):
    loan_list = str(row['Type_of_Loan'])
    comma_count = loan_list.count(",")
    if len(loan_list) < 3:   #refine > 3??
        return ""
    if comma_count == 0 and loan_list.count("Auto Loan") > 0:
        return loan_list.count("Auto Loan") 
   
    if comma_count > 0 and loan_list.count("Auto Loan") > 0:
        return loan_list.count("Auto Loan") 

df['Auto_Loan_Count'] = df.apply(get_Auto_Loan_count, axis=1)          

def get_Credit_Builder_count(row):
    loan_list = str(row['Type_of_Loan'])
    comma_count = loan_list.count(",")
    if len(loan_list) < 3:   
        return ""
    if comma_count == 0 and loan_list.count("Credit-Builder Loan") > 0:
        return loan_list.count("Credit-Builder Loan")    
    if comma_count > 0 and loan_list.count("Credit-Builder Loan") > 0:
        return loan_list.count("Credit-Builder Loan")
         
df['Credit_Builder_Count'] = df.apply(get_Credit_Builder_count, axis=1)

def get_Debt_Consolidation_count(row):
    loan_list = str(row['Type_of_Loan'])
    comma_count = loan_list.count(",")
    if len(loan_list) < 3:   
        return ""
    if comma_count == 0 and loan_list.count("Debt Consolidation Loan") > 0:
        return loan_list.count("Debt Consolidation Loan")    
    if comma_count > 0 and loan_list.count("Debt Consolidation Loan") > 0:
        return loan_list.count("Debt Consolidation Loan")

df['Debt_Consolidation_Count'] = df.apply(get_Debt_Consolidation_count, axis=1)

for i, row in df.iterrows():        #031323
    if "_" in row["Credit_Mix"]:
        df.loc[i,"Credit_Mix"] = df.loc[i,"Credit_Mix"].strip("_") 

for i, row in df.iterrows():   
    if "_" in row["Outstanding_Debt"]:
        df.loc[i,"Outstanding_Debt"] = df.loc[i,"Outstanding_Debt"].strip("_") 

df['Outstanding_Debt'] = df['Outstanding_Debt'].astype(float)

for i, row in df.iterrows():   
    if "_" in str(row["Amount_invested_monthly"]):
        df.loc[i,"Amount_invested_monthly"] = df.loc[i,"Amount_invested_monthly"].strip("_") 
    if len(str(row["Amount_invested_monthly"]))==0:
        df.loc[i,"Amount_invested_monthly"] =""
    if str(row["Amount_invested_monthly"])==10000:
        df.loc[i,"Amount_invested_monthly"] =".05"    
        
if df['Amount_invested_monthly'].isnull().any(): 
    # Replace missing or null values with "NA"
    df['Amount_invested_monthly'].fillna(".01", inplace = True)         

df['Amount_invested_monthly'] = df['Amount_invested_monthly'].astype(float)

for i, row in df.iterrows():   
    if len(str(row["Payment_Behaviour"]))<8:
        df.loc[i,"Payment_Behaviour"] ="NA"

if df['Monthly_Balance'].isnull().any(): 
    # Replace missing or null values with "NA"
    df['Monthly_Balance'].fillna(".01", inplace = True) 

df2 = df['Payment_Behaviour'  ]  #, 'Is_Credit_Builder_Loan'
df2.to_csv('C:\\Users\\\Robert\\.spyder-py3\\raw_data\\cc_classify_out_test2.csv')
# 'Credit_Mix', 'Outstanding_Debt', 'Outstanding_Debt', 'Credit_Utilization_Ratio', 'Payment_of_Min_Amount', 'Total_EMI_per_month'
# 'Amount_invested_monthly', 'Payment_Behaviour', 'Monthly_Balance'
    