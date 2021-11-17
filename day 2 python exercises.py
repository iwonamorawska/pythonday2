#!/usr/bin/env python
# coding: utf-8

# # Exercise 1
# Given a list as a parameter,write a function that returns a list of numbers that are less than ten


l_1 = [1,11,14,5,8,9]
new_l_1=[]
for i in l_1:
    if i<10:
        print(str(i))
        new_l_1.append(i)
print(new_l_1)   


# # Exercise 2
# Write a function that takes in two lists and returns the two lists merged together and sorted



l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

combined_list= sorted(l_1+l_2)
print(combined_list)
