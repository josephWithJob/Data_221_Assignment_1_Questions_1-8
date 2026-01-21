# Assignment 1, Question 4
# Joseph Krosel

from random import random

values = [random() for i in range(20)]
x = random()

sortedListFromValues = []
for i in values:
    if i >= x:
        sortedListFromValues.append(i)
print(sortedListFromValues)
