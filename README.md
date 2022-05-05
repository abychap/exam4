# Python script for substring analysis: BES539 Final Exam

Included in this repository is a python script (exam4.py) to analyze the amount of substrings within longer strings of genomic data. Genomic data is made up of strings containing "A", "C", "T", and "G", thus our alphabet is only 4 letters long. By reading a .txt file containing one or more strings of letters, this code will output files containing dataframes for each string. Each dataframe contains k values, substrings possible values, and observed substrings values. The k value is defined as the length of the substings. This can range from 1 to the whole length of the string. Substrings possible is the minimum amount of substrings possible for a given k value. The observed substrings is a count of the number of unique substrings that are actually observed out the those possible. The code will also print the linguistic complexity for each string. Linguistic complexity is the sum of the observed substrings for each value k possible in a given string divided by the sum of the possible substrings.

If a .txt file contained two strings, the user can expect the terminal output to appear as follows: 

string1 name
dataframe for string1
linguistic complexity for string1

string2 name
dataframe for string2
linguistic complexity for string2

Command to run this script in the terminal: python3 exam4.py stringofletters.txt

# Testing the python script 

This repository also includes a python file containing tests (test_exam4.py) for the exam4.py. These tests verify that the code is working correctly. Along with the tests, there are also assertions within each function to send errors when incorrect k values are entered (negative or fraction), or a string contains a character not found in the correct alphabet. 

Command to run tests: py.test test_exam4.py

# Sample text file provided 

A sample text file has been provided to run the script on (stringofletters.txt). The text file contains three strings:

ATTTGGATT
ACTGCAGCGCGATGATGAGAGAGATTTCAGGACACACATTGCCAAATTGAGGCAT
ATATATATATATATATA;

The output should be two dataframes and an error for the third string (it contains a character not included in the alphabet).

# Outputting dataframes to new files

exam4.py is written to print the name of the strings, the associated dataframes, and the linguistic complexity for each string in the .txt, but it will also export new .csv files containing the dataframes. After the code is run, the new dataframe files can be found in the directory that is currently being worked in. They will be saved as the name of each string. For example, if your .txt file contains two strings: ATAT and ATGC, the new csv files will be found under the names ATAT.csv and ATGC.csv. These dataframe files may take a second to load, so if they do not pop up immediately, give the script time to run fully. 
