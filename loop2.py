"""
Created on Sat Dec 19 14:37:20 2020

@author: Rajit aryan
"""
#taking input for the list in which we are going to add the out comes.
l=list(eval(input()))
#implementing the for loop
for i in l:
    l.append(i+5)
    print(l)
#as you run these lines you will see that the elements of the list keep aading up and every next list have more elements than the one before.
