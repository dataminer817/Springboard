USE [Kaggle]
GO
/*  This function returns the two words before the parameter @TargetWord and can be used in the SELECT list of the query   */
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE FUNCTION [dbo].[GetTwoWordsBefore]
(
    @InputString NVARCHAR(MAX),
    @TargetWord NVARCHAR(MAX)
)
RETURNS NVARCHAR(MAX)
AS
BEGIN
    DECLARE @TwoWordsBefore NVARCHAR(MAX);
    
    -- Create a table to hold the split words and their positions
    DECLARE @Words TABLE (
        Position INT IDENTITY(1,1),
        Word NVARCHAR(MAX)
    );
    
    -- Insert the split words into the table
    INSERT INTO @Words (Word)
    SELECT value 
    FROM STRING_SPLIT(@InputString, ' ')
    WHERE RTRIM(value) <> '';
    
    -- Find the position of the target word
    DECLARE @TargetPosition INT;
    SELECT @TargetPosition = Position
    FROM @Words
    WHERE Word = @TargetWord;
    
    -- If the target word is found and its position is greater than 2
    IF @TargetPosition IS NOT NULL AND @TargetPosition > 2
    BEGIN
        -- Get the two words before the target word
        SELECT @TwoWordsBefore = (
            SELECT STRING_AGG(Word, ' ') WITHIN GROUP (ORDER BY Position)
            FROM (
                SELECT Position, Word
                FROM @Words
                WHERE Position IN (@TargetPosition - 1, @TargetPosition - 2)
            ) AS TwoWordsBefore
        );
    END
    
    RETURN @TwoWordsBefore;
END;
