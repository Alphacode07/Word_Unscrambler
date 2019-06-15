# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 09:19:20 2019

@author: Surface
"""

#Software Starts

given_letters =[]

#Gathering input from the user

number_of_letters = int(input('How many letters are given? '))

#logic for transferring letters to empty list

count = 0
while count < number_of_letters:
    letter_data = input('What is the letter? ')
    given_letters.append(letter_data.upper())
    count+=1
    
