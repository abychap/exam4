#!/usr/bin/env python3

import pandas as pd #import to ba able to make dataframe at end 

#Define function for substrings possible: 
def substrings_possible_function(string_of_letters,k):
    '''input is a string of letters (containing only A,G,T, or C) and a k value (the length of new substrings wanted)
    returns the minimum possible number of substrings'''
    assert k > 0, 'k cannot be negative' #will give an error is negative k value is entered
    for letter in string_of_letters:
        assert letter in ["A","G","T","C"], 'string includes character outside of alphabet: characters can only be A,G,T, or C' #will give an error if any character is not a part of the correct alphabet
    assert type(k) is int, 'k must be a whole number' #will give an error if k is not an integer 
    substring_possible= len(string_of_letters) - k + 1
    combo_possible= 4**k
    return(min(substring_possible, combo_possible)) #there are two options for possible kmers above. we only want to return the lesser of the two. 

#Define function for substrings observed: 
def observed_substrings_function(string_of_letters,k):
    '''input is a string of letters (containing only A,G,T, or C) and a k value (the length of new substrings wanted)
    returns the number unique observed substrings'''
    newlst=[] #we make a blank list to add the unique values onto
    assert k > 0, 'k cannot be negative'
    for letter in string_of_letters:
        assert letter in ["A","G","T","C"], 'string includes character outside of alphabet: characters can only be A,G,T, or C'
    assert type(k) is int, 'k must be a whole number'
    observed_substrings= [string_of_letters[i:i+k] for i in range(0,len(string_of_letters),1)] #1 allows the loop to move character by character
    for i in range(0,len(observed_substrings)):
        if(len(observed_substrings) == k):
            observed_substrings.pop()
        for item in observed_substrings:
            if len(item) == k:
                newlst.append(item) #adds unique items to file
    new_set=set(newlst)
    unique_list=list([new_set]) #formats output into a list so that the length can be determined, and therefore the amount of unique observed kmers. 
    for x in unique_list:
        return(len(x))   

#Define function for creating a dataframe: 
def create_df(string_of_letters): 
    '''input is a string of letters (containing only A,G,T, or C)
    returns data frame containing the range of possible k values, and the number of possible and observed substrings for each k value'''
    obslist=[] #we start by making blank lists to append onto as we loop through the string with each function. The output of he functions as k increases will be added to these lists
    poslist=[]
    kvalues=[] 
    for k in range(1,len(string_of_letters)+1):  
        obskmers= observed_substrings_function(string_of_letters, k)
        obslist.append(obskmers)
    for k in range(1,len(string_of_letters)+1):    
        poskmers= substrings_possible_function(string_of_letters, k)
        poslist.append(poskmers)
    for k in range(1,len(string_of_letters)+1):
        kvalues.append(k)
    data=({'k' : kvalues,
          'observedkmers': obslist,
          'possiblekmers': poslist }) #collecting the data for the dataframe
    df=pd.DataFrame(data) #using panda to make the data frame
    df.to_csv((string_of_letters)+'.csv') #outputting the data frames to csv files named after each string (ex. ATAT exported as ATAT.csv) They may take a second to load. 
    return(df) 

#Define function for linguistic complexity: 
def ling_comp(string_of_letters):
    '''input is a string of letters (containing only A,G,T, or C)
    returns the linguistic complexity: the sum of the number of substrings observed for each k divided by the sum of the substrings possible for each k'''
    obslist_ling=[] #just like in the df function, we start with blank lists to append onto as the loops progress
    poslist_ling=[]
    for k in range(1,len(string_of_letters)+1):  
        obskmers_ling= observed_substrings_function(string_of_letters, k)
        obslist_ling.append(obskmers_ling) #creating list of observable kmers ouput 
    for k in range(1,len(string_of_letters)+1):    
        poskmers_ling= substrings_possible_function(string_of_letters, k)
        poslist_ling.append(poskmers_ling) #creating list of possible kmers ouput 
    return((sum(obslist_ling))/(sum(poslist_ling))) #dividing the sum of observed by the sum of the possible 


#The following code will be run if the script itself is being run. This code will not run when the .py is being tested 

if __name__ == '__main__':
    string_of_letters_full= 'stringofletters.txt'
    with open(string_of_letters_full, "r") as f:
        for eachline in f:   
            eachline = eachline.strip()
            print(eachline) #I had the code print each line to keep the datframes organized when they print to the terminal 
            print(create_df(eachline)) #prints the df to the terminal 
            print(ling_comp(eachline)) #prints the linguistic complexity
            
#New files containing the dataframes will also be saved in the directory being worked in as each (string_of_letters).csv. This is done within the dataframe function. (see comments on line 57). They may take a second to load. 