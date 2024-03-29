USE [Kaggle]
GO
/*
  This function returns the word before the parameter @TargetWord and can be used in the SELECT list of the query
*/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE FUNCTION [dbo].[GetWordBefore]
(
    @InputString NVARCHAR(MAX),
    @TargetWord NVARCHAR(MAX)
)
RETURNS NVARCHAR(MAX)
AS
BEGIN
    -- Add a space around the input string and target word
    SET @InputString = ' ' + @InputString + ' ';
    SET @TargetWord = ' ' + @TargetWord + ' ';
    
    -- Find the position of the target word
    DECLARE @WordPos INT = CHARINDEX(@TargetWord, @InputString);

    -- If target word is found
    IF @WordPos > 0
    BEGIN
        -- Get the substring before the target word
        DECLARE @BeforeSubstr NVARCHAR(MAX) = LEFT(@InputString, @WordPos - 1);

        -- Find the position of the last space in the before substring to get the start position of word before
        DECLARE @LastSpaceBefore INT = LEN(@BeforeSubstr) - CHARINDEX(' ', REVERSE(@BeforeSubstr)) + 1;

        -- Get the word before
        DECLARE @WordBefore NVARCHAR(MAX) = LTRIM(RIGHT(@BeforeSubstr, LEN(@BeforeSubstr) - @LastSpaceBefore + 1));

        -- Return the word before
        RETURN @WordBefore;
    END

    -- Return NULL if the target word is not found
    RETURN NULL;
END;
