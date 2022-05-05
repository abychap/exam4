#!/usr/bin/env python3

from exam4 import *

#make sure length of read in string is correct 

#observed: 
    
def test_observed_k9(): #when the length of the string is equal to the k value, the program should always return 1 for observed
    observed_substrings = observed_substrings_function('ATTTGGATT', 9)
    assert observed_substrings == 1
    
def test_observed_k10(): #in this case, the k value entered is longer than the length of the string, so the program should give a zero
    observed_substrings = observed_substrings_function('ATTTGGATT', 10)
    assert observed_substrings == 0
    
def test_observed_k14():
    observed_substrings = observed_substrings_function('ATATATATATATATATA', 14)
    assert observed_substrings == 2
    
def test_observed_k1(): #when the k value is 1, the observed shold reflect how many of the alphabet letters are present (in this case only 3)
    observed_substrings = observed_substrings_function('ATTTGGATT', 1)
    assert observed_substrings == 3
    

#possible:


def test_possible_k2(): 
    substring_possible = substrings_possible_function('ATTTGGATT', 2)
    assert substring_possible == 8
    
def test_possible_k7(): #possible kmers should not take away any repetition 
    substring_possible = substrings_possible_function('ATATATATATATATATA', 7)
    assert substring_possible == 11
    
def test_possible_k17(): #when the length of the string is equal to the k value, the program should always return 1 for possible
    substring_possible = substrings_possible_function('ATATATATATATATATA', 17)
    assert substring_possible == 1


#linguistic 

def test_ling_com():
    linguistic_complexity = ling_comp('ATTTGGATT')
    assert linguistic_complexity == 0.875

def test_ling_com2(): #the number for a string with many repeats should be lower. Checking to make sure this is the case and that no repetition is being included by the observed. 
    linguistic_complexity = ling_comp('ATATATATATATATATA')
    assert linguistic_complexity == 0.2357142857142857
    
def test_ling_com3():
    linguistic_complexity = ling_comp('ACTGCAGCGCGATGATGAGAGAGATTTCAGGACACACATTGCCAAATTGAGGCAT')
    assert linguistic_complexity == 0.9738111647139903

