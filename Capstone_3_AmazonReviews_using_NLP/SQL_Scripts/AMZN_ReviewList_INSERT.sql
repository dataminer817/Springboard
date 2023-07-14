/*
  This script appends the Review data from the staging table into a flattened relational table where all
  info is aligned on the same row; the derived columns where " t3.RowNum = t1.RowNum +1 and t3.[ID]=t1.[ID] "
  is the logic that flattens the rows
*/
WITH cteTransform AS (
SELECT ROW_NUMBER() OVER(PARTITION BY ID ORDER BY (SELECT NULL)) RowNum
      , [ID]
      , [key]
      , [value]
	  , CASE WHEN [key]='review_meta' THEN [value] ELSE '' END AS K
	  , CASE WHEN [key]='review_star' THEN [value] ELSE '' END AS Rating
	  , CASE WHEN [key]='review_body' THEN [value] ELSE '' END AS V
FROM [Kaggle].[dbo].[Aug0922_reviewlist] 
)
--INSERT INTO [Apr0922_sent_review]  ( RowNum, [ID], [Sentiment], [Review] )
SELECT  RowNum, [ID]--, K 
, ( SELECT Substring(Rating,27,1) FROM cteTransform t3 where t3.RowNum = t1.RowNum +1 and t3.[ID]=t1.[ID] ) Sentiment
, ( SELECT V FROM cteTransform t2 where t2.RowNum = t1.RowNum +2 and t2.[ID]=t1.[ID] ) Review 
FROM cteTransform t1
WHERE K <>''
ORDER BY ID, t1.RowNum
