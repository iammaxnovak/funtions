# -*- coding: utf-8 -*-

def intersect(s1, s2):
    res = []
    for x in s1:
        if x in s2:
            res.append(x)
    return res

import random

def password(length):
    pw = str()
    characters = "abcdefghijklmnopqrstuvwxyz" +"0123456789"
    for i in range(length):
        pw = pw + random.choice(characters)
    return(pw)

def is_vowel(letter):
    if letter in "aeiouy":
        print(True)
    else:
        print(False)
        
def is_vowel_2(letter):
    if type(letter) == int:
        letter = str(letter)
    if letter in ("aeiou"):
        return(True)
    else:
        return(False)
    
def factorial(n):
    if n == 0:
        return 1
    else:
        N=1
        for i in range(1, n+1):
            N= N+i
        return(N)
            