#!/usr/bin/env python3

from exam4 import *

#make sure length of read in string is correct 

#observed: 
    
def test_observed_k9():
    observed_substrings = observed_substrings_function('ATTTGGATT', 9)
    assert observed_substrings == 1
    
def test_observed_k10():
    observed_substrings = observed_substrings_function('ATTTGGATT', 10)
    assert observed_substrings == 0
    
def test_observed_k14():
    observed_substrings = observed_substrings_function('ATATATATATATATATA', 14)
    assert observed_substrings == 2
    
def test_observed_k1():
    observed_substrings = observed_substrings_function('ATTTGGATT', 1)
    assert observed_substrings == 3
    

#possible:


def test_possible_k2():
    substring_possible = substrings_possible_function('ATTTGGATT', 2)
    assert substring_possible == 8
    
def test_possible_k7():
    substring_possible = substrings_possible_function('ATATATATATATATATA', 7)
    assert substring_possible == 11
    
def test_possible_k17():
    substring_possible = substrings_possible_function('ATATATATATATATATA', 17)
    assert substring_possible == 1


#linguistic 

def test_ling_com():
    linguistic_complexity = ling_comp('ATTTGGATT')
    assert linguistic_complexity == 0.875

def test_ling_com2():
    linguistic_complexity = ling_comp('ATATATATATATATATA')
    assert linguistic_complexity == 0.2357142857142857
    
def test_ling_com3():
    linguistic_complexity = ling_comp('ACTGCAGCGCGATGATGAGAGAGATTTCAGGACACACATTGCCAAATTGAGGCAT')
    assert linguistic_complexity == 0.9738111647139903

