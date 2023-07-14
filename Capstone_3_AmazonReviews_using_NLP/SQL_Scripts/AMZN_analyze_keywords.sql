/*  This SQL script queries the [ID_Sentiments_keywords] table keywords column and scans the table output
    when passed a parameter: @KeyWord with values such as:  quality value   worth  price  satisfaction  
	Four user defined SQL functions locate the Keyword and then return the first and second word before the 
	keyword and the first and second word after the keyword in grid view                                     */

DECLARE @KeyWord as VarChar(20) ='quality';    
SELECT  P.Category
	  , P.Product_Name
      , [Sentiment]
      , [keywords], dbo.GetWordBefore([Keywords], @KeyWord)  Word_Before
	  , @KeyWord [KeyWord]
	  , ISNULL(dbo.GetWordAfter([Keywords], @KeyWord),'') Word_After
	  , ISNULL(dbo.GetTwoWordsBefore([Keywords], @KeyWord),'') TwoWordsBefore
	  , @KeyWord [KeyWord]
	  , ISNULL(dbo.GetTwoWordsAfter([Keywords], @KeyWord),'') TwoWordsAfter
FROM [Kaggle].[dbo].[ID_Sentiments_keywords] kw
JOIN Aug0922 P
  ON kw.ID=p.ID
WHERE CHARINDEX(@KeyWord,keywords)>0  and sentiment in (5,1)


