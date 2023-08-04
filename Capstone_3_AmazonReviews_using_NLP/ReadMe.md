# Amazon Customer Reviews Text Analysis using Python NLP and SQL

In the rapidly evolving domain of e-commerce, understanding customer sentiment is pivotal for enhancing user experience and refining product offerings. This report delves deep into a cutting-edge Natural Language Processing (NLP) project that sets out to classify the sentiment levels of Amazon Customer Reviews, spanning from a score of 1, signifying dissatisfaction, to 5, indicating commendable satisfaction. This solves the problem of delivering good or excellent customer satisfaction across different products to find out what works well and what does not, what products are made with quality and where are areas for improvement. To achieve this intricate task, two machine learning models were employed: the Random Forest Classifier and the Support Vector Machine classifier, each bringing their unique strengths to the fore. Prior to model deployment, rigorous data wrangling and exploratory data analysis (EDA) were carried out, harnessing the power and versatility of both SQL and Python. The harmonious confluence of these methodologies and tools not only refined our dataset but also paved the way for deeper, more accurate sentiment analysis.

## Initial Data Wrangling: extract, transform, load the source CSV files
The first step is the data wrangling and loading of the source files which were downloaded from the Kaggle web site. An immediate complication was to extract the list of dictionaries from the Review column, for each row, in the CSV and that took custom Python and SQL scripts for import and further processing.

### Step 0:
Import the raw data files from Kaggle at:
[https://www.kaggle.com/datasets/tigboatnc/amazon-all-categories-best-sellers-reviews](https://www.kaggle.com/datasets/tigboatnc/amazon-all-categories-best-sellers-reviews)

### Step 1: 
Import CSV file from Kaggle into a SQL database table for part of EDA steps later.

### Step 2: 
Run Python script to extract Review column info in the original CSV file into a separate table: a separate table is needed because the original Review column is a list data structure with many embedded dictionaries in the list of Review column data. All Python files for Data Wrangling and EDA tasks are in the folder listed [here](https://github.com/dataminer817/Springboard/Capstone_3_AmazonReviews_using_NLP/Python_Scripts)

The Python script extracts the key and values of the nested dictionaries in the list into a CSV:

### Step 3:  
The Step 2 table is imported into SQL database as a staging table and a Common Table Expression query is run that will join to non-matching keys to output a properly formatted, "flattened" relational structure to be appended to a production SQL database table that can be queried. All SQL files for Data Wrangling and EDA tasks are in the folder listed [here](https://github.com/dataminer817/Springboard/Capstone_3_AmazonReviews_using_NLP/SQL_Scripts)

SQL script inserts the staging table info into a format with Sentiment score and its Review text on the same line that can now be queried:

### Python script to extract keywords from the Reviews column:

The RAKE-NLTK library provides a simple API for extracting keywords from text. The following code shows how to extract the top 10 keywords from a piece of text:

Sample output after the keyword extract script has been executed:

The Jupyter file `amazon_review_nlp.ipynb` is used for initial Python NLP functions such as stemming, lemmatization, tokenization, stop word removal and extracting larger pieces of Review text into smaller strings of Keywords for Frequency analysis in the SQL database.

## Exploratory Data Analysis using Python and SQL

An early phase of the exploratory data analysis phase was querying the Review data which could then be appended to a separate keywords table as well as a separate dictionary table for “good” and “bad” words. It was an iterative process of passing keywords as parameters and then visually reading the records returned.

The SQL script `Get_Aggregate_Count_Of_WordBefore_Keyword_By_Category.sql` calls a user defined function: `GetWordBefore`, which extends the basic SQL functionality. This function returns the word before the parameter: `@TargetWord` (Keyword: quality) and can be used in the SELECT list of the query to scan the multi-word string Keywords column:
