# Credit Card Credit Score Prediction: Machine Learning Classification
## The Problem Statement and Project Goal:
The project goal of this credit card credit scoring machine learning classification exercise is to discover a combination of data attributes that can be calculated by a credit card issuing company to derive  a Credit Card score that identifies good credit scores and bad credit scores that will minimize credit card losses and defaults by 20% and predict credit card usage level within a range of 15% to improve credit card profitability within 3 months of implementation.
## The Data Source:
The Kaggle website hosts the original credit card datasets on their website as one of their online competitions. Here, the data was downloaded from the Kaggle website. Following are the data fields in the dataset, which are going to be read in the Pandas data frame after a number of data transformations are made since data is very rarely ready for use without preliminary data cleaning and standardizing. 

![image](https://github.com/dataminer817/Springboard/assets/44590198/93c8e260-3263-4f80-953f-e1cd90778b89)

## Data Cleaning
The data cleaning and preprocessing steps are setting the missing values to their mean or median values for the respective columns as well as setting outliers to the mean. There were also some re-scaling of numerical data and the target Y credit scores had to be converted from text to numeric with values 1 = Poor, 2 = Standard, 3 = Good.   At this data cleaning and standardizing phase dummy variables were created.

Python code snippet that shows Occupation column conversion:

![image](https://github.com/dataminer817/Springboard/assets/44590198/9bfd2a2f-9a99-4bd1-875b-95a7156482cd)
 
 
Output for the original Occupation column after dummy variables have been encoded:
 
 ![image](https://github.com/dataminer817/Springboard/assets/44590198/916f0252-486a-4770-a094-31a230c16923)
 

Columns needing their magnitude re-scaled were done using the Standard Scaler library:

![image](https://github.com/dataminer817/Springboard/assets/44590198/f4882f92-8741-427f-a5a4-15aa476b6a77)

 
The last step of data cleaning and preprocessing is the creation of train and test files for the credit card data:

![image](https://github.com/dataminer817/Springboard/assets/44590198/7e0d96e2-3bf7-4e9f-86b3-5653fa5874bd)


