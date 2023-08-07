# Amazon Customer Reviews Text Analysis using Python NLP and SQL

In the rapidly evolving domain of e-commerce, understanding customer sentiment is crucial for enhancing user experience and refining product offerings. This report delves deep into a cutting-edge Natural Language Processing (NLP) project that sets out to classify the sentiment levels of Amazon Customer Reviews, spanning from a score of 1, signifying dissatisfaction, to 5, indicating commendable satisfaction.  This solves the problem of delivering good or excellent customer satisfaction across different products to find out what works well and what does not, what products are made with quality and where are areas for improvement.  To achieve this intricate task, two machine learning models were employed: the Random Forest Classifier and the Support Vector Machine classifier, each bringing their unique strengths to the fore. Prior to model deployment, rigorous data wrangling and exploratory data analysis (EDA) were carried out, harnessing the power and versatility of both SQL and Python. The harmonious confluence of these methodologies and tools not only refined and augmented our dataset but also paved the way for deeper, more accurate sentiment analysis.

## Initial Data Wrangling: extract, transform, load the source CSV files

The first step is the data wrangling and loading of the source files which were downloaded from the Kaggle web site and most columns were easily imported into a SQL database.  An immediate complication was to extract the list of dictionaries from the Review column, for each row, in the CSV and that took custom Python and SQL scripts for import and further processing.  

A Python script was executed to extract Review column info contained in the original CSV file into a separate table: a separate table is needed because the original Review column is a list data structure with many embedded dictionaries in the list of Review column data.

The Python script extracts the key and values of the nested dictionaries in the list into a CSV file, which can be imported into a SQL database though this format is not optimal for querying and is not in compliance with the relational model; output is below:

![image](https://github.com/dataminer817/Springboard/assets/44590198/ffbc8eb5-4118-4ef9-ab6d-a1806b18dbde)

 All SQL files for Data Wrangling and EDA tasks are in the folder listed [here](https://github.com/dataminer817/Springboard/Capstone_3_AmazonReviews_using_NLP/SQL_Scripts)

Step 3:  The Step 2 table is imported into SQL database as a staging table and a Common Table Expression query is run that will join to non-matching keys to output a properly formatted, "flattened" relational structure to be appended to a production SQL database table that can be queried (All SQL files for Data Wrangling and EDA tasks are in the folder listed below).	

The SQL script employed below uses a derived table to “query the query” and inserts the staging table info into a format with Sentiment score and its Review text on the same line that can now be queried more efficiently:

![image](https://github.com/dataminer817/Springboard/assets/44590198/a693f9f2-8996-4851-ae1a-337ea77fe7f0)



### Python script to extract keywords from the Reviews column:

The RAKE-NLTK library provides a simple API for extracting keywords from text. The following output shows a new column, ‘keywords’ derived from the ‘Review’ column with the use of the “extract_keywords_rake” function using Python.

Sample output after the keyword extract script has been executed:

![image](https://github.com/dataminer817/Springboard/assets/44590198/93db7493-5782-43ec-bb42-2dacabcdc231)


The Jupyter file amazon_review_nlp.ipynb is used for initial Python NLP functions and data wrangling tasks such as  stemming, lemmatization, tokenization, stop word removal and extracting larger pieces of Review text into smaller strings of Keywords for Frequency analysis in the SQL database.  

## Exploratory Data Analysis using Python and SQL

An early phase of the exploratory data analysis phase was querying the Review data which could then be appended to a separate keywords table as well as a separate dictionary table for “good” and “bad” words.  It was an iterative process of passing keywords as parameters and then visually reading the records returned. Another SQL table was created that appends each word as a separate record, along with Category and Sentiment as separate columns to query for aggregate counts.

The SQL script Get_Aggregate_Count_Of_WordBefore_Keyword_By_Category.sql calls a user defined function: GetWordBefore, which extends the basic SQL functionality.  This function returns the word before the parameter: @TargetWord (Keyword: quality) and can be used in the SELECT list of the query to scan the multi-word string Keywords column:

![image](https://github.com/dataminer817/Springboard/assets/44590198/1c703a92-29eb-4081-a0fa-92bdc6543929)

Below is output of key phrases that denote good or bad sentiment when scanning through the keywords column of the SQL table:

![image](https://github.com/dataminer817/Springboard/assets/44590198/8a7fee7a-480b-477a-b02a-cdbe070f24cd)

SQL Script that gets keyword counts across product categories:

![image](https://github.com/dataminer817/Springboard/assets/44590198/0f6eccb7-3127-4517-98a8-677941d57a43)

From a Marketing Research perspective this is the most useful and powerful SQL script to view and evaluate textual sentiment:  “quality” is passed in as a parameter and two user defined functions return the two words before the parameter and two user defined functions return the two words after the parameter.  Thousands of rows can be scanned by the script in seconds and then read by the Marketing Data Science team.  

![image](https://github.com/dataminer817/Springboard/assets/44590198/4ddd4fec-be8c-4437-9749-8df63d528405)

## Pre-processing in Python:

One of the preliminary  preprocessing steps is to implement the NLTK stopwords function, which is a script to eliminate common words such as ‘the’,  ‘and’, etc. to facilitate text processing.  Also, listed below, is a lemmatizer function which converts different forms of a word down to its root structure such as “running” to “run.”  Also as a preprocessing step is converting all words to lowercase.  These were steps that were executed before the new column ‘keywords’ was created from the ‘Review’ column.  A Python script was also run to create train and test datasets for the Machine Learning to process.

 
For purposes of enabling Python’s NLP: Below is the output of the Review column after all of the data wrangling and pre-processing has completed:

![image](https://github.com/dataminer817/Springboard/assets/44590198/e23d397b-416e-4f3a-9d25-a654e759e51f)

## Machine Learning Modeling: Random Forest and Support Vector Machine text classifiers

For the initial Natural Language Processing Machine Learning Text Classifier in Python the Random Forest Classifier was executed along with the Support Vector Machines (SVM) text classifier to analyze the thousands of records of Amazon customer review data with sentiments ranging from 1 - 5.

When running the Random Forest classifier the overall Accuracy: 0.6532; this means it correctly predicts the sentiment of reviews about 65.3% of the time.  The output of the Precision, Recall and F1 Scores for Sentiments 1 - 5:

![image](https://github.com/dataminer817/Springboard/assets/44590198/ea7e8a61-15d1-4b70-8613-0790b4a7328f)

The confusion matrix shows how many times the classifier correctly and incorrectly classified the data. The confusion matrix is a table with five dimensions: the predicted sentiment and the actual sentiment. The table shows the number of times the classifier predicted each sentiment, and the number of times the classifier incorrectly predicted each sentiment.

Sentiment 1: The model has a high precision (0.81), meaning that when it predicts a review as sentiment 1, it's correct 81% of the time. The recall is 0.49, which means the model only identifies 49% of all actual sentiment 1 reviews. The F1-score is the harmonic mean of precision and recall and is 0.61, reflecting a balance between precision and recall.

Sentiment 2: The precision is perfect (1.00), which means when the model predicts sentiment 2, it's always correct. However, the recall is very low (0.08), meaning that the model only captures 8% of actual sentiment 2 reviews. The low recall leads to a low F1-score (0.14).

Sentiment 3: The precision is high (0.79), but the recall is very low (0.12), leading to a low F1-score (0.21). This means that when the model predicts sentiment 3, it's mostly correct, but it fails to identify a significant portion of actual sentiment 3 reviews.

Sentiment 4: The precision is decent (0.70), but the recall is low (0.21), leading to a low F1-score (0.33). This indicates that the model struggles to correctly identify sentiment 4 reviews.

Sentiment 5: The precision is 0.65, which means that out of all reviews the model identifies as sentiment 5, 65% are correctly identified. The recall, however, is very high (0.98), meaning the model is able to correctly identify 98% of actual sentiment level 5 reviews. The F1-score is quite high (0.78), reflecting a good balance between precision and recall for this class.model is able to correctly identify 98% of actual sentiment level 5 reviews. The F1-score is quite high (0.78), reflecting a good balance between precision and recall for this class.

The classifier is performing quite well on classes 1 and 5, especially on class 5. It struggles more with classes 2, 3, and 4, likely because these classes are still underrepresented in the data. The second dataset of Amazon customer reviews were added for those sentiments 1 - 4 to even out the distribution to remedy the underrepresentation.
 

To benchmark the results of the Random Forest Classifier, the Support Vector Machines (SVM) text classifier was also executed against the Amazon Customer Review dataset.

Overall, the Classifier Accuracy is 0.6634 for the Support Vector Machines (SVM) text classifier and the Precision, Recall, F1-Score values are shown in the table below:

![image](https://github.com/dataminer817/Springboard/assets/44590198/bc6ebf6a-1d70-4d15-bd61-6562b761ebdd)

Sentiment 1: The precision is 0.16, which means when the model predicts sentiment 1, it's correct 16% of the time. The recall is 0.09, meaning the model correctly identifies only 9% of actual sentiment 1 reviews. The F1-score is 0.11, reflecting a balance between precision and recall but suggesting that the model performs poorly for this class.

Sentiment 2: The model's performance for this class is very poor. Both precision and recall are 0, and as a result, the F1-score is also 0. This means the model neither predicts this class correctly nor identifies the actual instances of this class.

Sentiment 3: The model's performance for this class is also poor, with a precision of 0.05, a recall of 0.01, and a very low F1-score (0.01). This means that the model rarely predicts sentiment 3 correctly and fails to identify most of the actual sentiment 3 reviews.

Sentiment 4: The precision is 0.17, meaning the model is correct 17% of the time when it predicts sentiment 4. However, the recall is very low at 0.06, suggesting the model fails to identify most actual sentiment 4 reviews. The F1-score is 0.08, indicating a poor balance between precision and recall.

Sentiment 5: The precision is 0.56, indicating that when the model predicts sentiment 5, it's correct 56% of the time. The recall is high at 0.86, meaning the model captures 86% of actual sentiment 5 reviews. The F1-score is relatively high at 0.68, reflecting a decent balance between precision and recall for this class.

## Hyperparameter tuning and parameter implications of the optimal model

When comparing the two model’s results it was clear the Random Forest Classifier could be improved by conducting Hyperparameter tuning. This process optimized the model by searching for the most effective combination of parameters, which helped improve our model's predictive power. After finding the optimal parameters, we re-executed the Random Forest Classifier code, which generated an improvement in the Accuracy, Precision, Recall, and F1-Score. 

![image](https://github.com/dataminer817/Springboard/assets/44590198/fb25669a-25ef-4d5b-9c24-d011146b7b13)

These scores show how the model performs on each sentiment class after using the optimal parameters derived from hyperparameter tuning.

Sentiment 1: The model has a precision of 0.90, which means that when the model predicts an instance to be in class 1, it is correct 90% of the time. However, the recall of 0.40 indicates that the model is only able to correctly identify 40% of the total true class 1 instances. The F1-score is a harmonic mean of precision and recall, giving an overall measure of the model's performance in identifying class 1 instances. An F1-score of 0.55 is fairly good but still indicates there's room for improvement, mainly on improving the recall.

Sentiment 2: The model is perfect in precision (1.00) for this class, meaning every time it predicts an instance to be in class 2, it is always correct. However, the recall is extremely low at 0.05, indicating it is only identifying 5% of the actual class 2 instances correctly. The resulting F1-score is 0.09, which is poor and suggests that although the model's predictions for class 2 are accurate, it is missing a lot of actual class 2 instances.

Sentiment 3: Similar to class 2, the precision for class 3 is also perfect (1.00), but the recall is very low (0.04), resulting in a poor F1-score of 0.08. This suggests that the model is not good at identifying class 3 instances, even though its predictions are precise when it does make them.

Sentiment 4: The model has a good precision score (0.89), but the recall is very low (0.10), leading to a poor F1-score of 0.18. This implies that the model is struggling to identify instances of class 4, despite its predictions being accurate when it does.

Sentiment 5: The model has a lower precision for this class (0.62), meaning that when it predicts an instance to be class 5, it is correct about 62% of the time. However, the recall is perfect (1.00), indicating that the model is identifying all instances of class 5 correctly. The F1-score is 0.76, which is quite good and suggests that the model is performing best on this class.

In general, these results suggest that the model is performing best on sentiment 5, but struggling with the other classes, particularly 2, 3, and 4. This could be due to class imbalance if there are significantly more instances of class 5 in the data, or it could suggest that the features distinguishing these classes are not being effectively captured by the model. A further study in the next iteration would be to consider techniques to address class imbalance or feature engineering to improve the model's performance on the other classes.


## Marketing Research: AB Tests of Good and Bad Dictionary Words For Sentiments 1 - 5

An A/B test was also executed to analyze the Amazon customer review data of various products. An A/B test is a statistical method used to compare two or more groups (variants) to determine if there are significant differences in their performance or outcomes. In the context of analyzing customer review data, the A/B test is used here to compare pairs ‘good’ and ‘bad’ or ‘good’ and ‘better’ words from the Amazon Customer Review table of words and then evaluate their t-statistics and determine if the P-value is significant.  For example, when viewing control group word:  horrible and treatment group word:  recommend T-statistic is -14.79010759243405
And P-value: 2.5432250103042375e-46.  A much more subtle but still meaningful example is: control group word: like and treatment group word: love where T-statistic: -14.44781853060049 and P-value: 9.608168116118143e-47.  A negative T-statistic (-14.44781853060049) suggests that the mean sentiment score of the treatment group (those reviews containing the word "love") is greater than the mean sentiment score of the control group (those reviews containing the word "like"). In other words, reviews that contain the word "love" tend to have higher sentiment scores than reviews that contain the word "like".

The p-value is extremely small (9.608168116118143e-47), which is much less than the typical threshold of 0.05 used in statistical testing. This provides strong evidence against the null hypothesis (which states that there's no difference between the groups). Therefore, we can reject the null hypothesis and conclude that there's a statistically significant difference between the mean sentiment scores of the two words (groups): “like” and “love.”

Similarly, an AB Test was run for the words “cheap” and “quality”, where “cheap” can have two meanings; it can mean inexpensive or it can mean cheaply made which implies a lack of quality.

![image](https://github.com/dataminer817/Springboard/assets/44590198/fb1ce91d-605d-4f67-bd55-e1e721daf704)
 
The AB Test for keywords  “cheap” versus “quality” underscore the need to have humans read the text for ambiguity since cheap can have either good or bad connotations.

In conclusion, the Amazon customer reviews project utilized a wide variety of analytical techniques to delve into thousands of rows of textual data. The initial stages of the project leveraged a great deal of data wrangling and exploratory data analysis (EDA) in Python but also SQL for database queries and data extraction. We further harnessed Python’s robust data manipulation libraries to refine our data and conduct insightful EDA.  Since it is text data being analyzed, SQL was very helpful in looking at the words before and after certain keywords such as “cheap” versus “quality” and “made in China” versus “made in USA” by querying thousands of records and enabling a quick read by humans.  This combination of SQL and Python demonstrated a synergistic effect, allowing us to derive more nuanced insights from the data and prepare it for machine learning algorithms. 

The main Machine Learning models we employed were the Random Forest Classifier and the Support Vector Machine Classifier. The Random Forest Classifier, known for its robustness and ability to handle large datasets with high dimensionality, performed admirably. It provided us with a strong baseline from which to compare our other models. On the other hand, the Support Vector Machine Classifier, known for its effectiveness in high-dimensional spaces and its versatility, added another layer of depth to our analysis.

The Amazon customer reviews project demonstrated the power and versatility of NLP in machine learning and the significant role it can play in understanding customer sentiment. Although the machine learning models exhibited varying degrees of success for sentiment scores 2, 3 and 4, they both performed very well on sentiment score 5. The entire process, from data wrangling and EDA through to the application of machine learning, highlighted the potential to harness customer review data to gain meaningful insights and guide strategic decision-making. The project was a testament to the power of data-driven insights but it was also a reminder that human intervention would still need to be involved to read the text for when certain words have two meanings (i.e. “cheap” or “bad”) or are otherwise ambiguous. Future work could involve incorporating more advanced NLP techniques or other machine learning models to further enhance the analysis and improve model performance.

