# HomeworkAssignment6_Python
Question1: If you are given three sticks, you may or may not be able to arrange them in a triangle. For example, if one of the
sticks is 12 inches long and the other two are one inch long, it is clear that you will not be able to get the short
sticks to meet in the middle.
 Write a function named is_triangle that takes three integers as arguments, and that prints either “Yes” or “No,”
depending on whether you can or cannot form a triangle from sticks with the given lengths.
 Write a Python program that prompts the user to input three stick lengths, converts them to integers, and uses
the is_triangle function to check whether sticks with the given lengths can form a triangle. The result should be
printed to the console

Question 2:
 Grady Ward collected and contributed a word list to the public domain as part of the Moby lexicon project. It is a
list of 113,809 official crosswords; that is, words that are considered valid in crossword puzzles and other word
games. A file containing Ward’s list of crosswords is available for download from clickUP, called Crosswords.txt.
 In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter “e.”
Since “e” is the most common letter in English, that’s not easy to do.
 Write a Python program that reads in all the words contained in the Crosswords.txt file and computes the
percentage of words in that do not contain the letter “e”. The result should be printed to the console.
 Your program should contain a function called ‘has_no_e’. It takes one string as argument and returns true if that
string does not contain the letter ‘e’ or false if it does.

Question 3:
 Write a Python program that reads in a csv file, detects duplicate rows and generates a new csv file with all
duplicates removed. Duplicate rows should be identified on composite of all columns.
 Your program should output the original number of records, the number of duplicates, the name of the new
csv file and the number of records contained in the new csv file.

Question 4:
 The following CSV files are available on clickUP:
o covid.csv
o titanic.csv
o tips.csv
o mpg.csv
 Choose one of these files as your data source, then write code to perform each of the following operations:
o Import the data from your CSV file into a Pandas Dataframe.
o Add a new calculated column to the dataframe.
o Create a subset of the data based on a condition.
o Calculate the correlation coefficient between two columns and show whether a significant correlation exists
(correlation coefficient values less than +0.8 or greater than -0.8 are not considered significant).
o Generate a data visualisation from the data in your data frame. Your visualisation must be sensibly thought
out (i.e. answer a reasonable business question) and it must have customised styling (e.g. title, axis labels,
legend, colors, etc.).
