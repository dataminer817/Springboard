USE [Kaggle]
GO
/* This function returns the word after the parameter @TargetWord and can be used in the SELECT list of the query */
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE FUNCTION [dbo].[GetWordAfter]
(
    @InputString NVARCHAR(MAX),
    @TargetWord NVARCHAR(MAX)
)
RETURNS NVARCHAR(MAX)
AS
BEGIN
    -- Add a space at the end of the input string
    SET @InputString = @InputString + ' ';

    -- Find the position of the target word
    DECLARE @WordPos INT = CHARINDEX(@TargetWord, @InputString);

    -- If target word is found
    IF @WordPos > 0
    BEGIN
        -- Calculate length after the target word
        DECLARE @LengthAfter INT = LEN(@InputString) - @WordPos - LEN(@TargetWord);

        -- If there are characters after the target word
        IF @LengthAfter > 0
        BEGIN
            -- Get the substring after the target word
            DECLARE @AfterSubstr NVARCHAR(MAX) = SUBSTRING(@InputString, @WordPos + LEN(@TargetWord) + 1, @LengthAfter);

            -- Find the position of the first space in the after substring to get the end position of the word after
            DECLARE @FirstSpaceAfter INT = CHARINDEX(' ', @AfterSubstr);

            -- Check if there's space character in the remaining string
            IF @FirstSpaceAfter > 0
            BEGIN
                -- Get the word after
                DECLARE @WordAfter NVARCHAR(MAX) = SUBSTRING(@AfterSubstr, 1, @FirstSpaceAfter - 1);

                -- Return the word after
                RETURN LTRIM(RTRIM(@WordAfter));
            END
            -- If no space character is found, return the whole remaining string
            ELSE
                RETURN LTRIM(RTRIM(@AfterSubstr));
        END
    END

    -- Return NULL if the target word is not found or there are no characters after it
    RETURN NULL;
END;
