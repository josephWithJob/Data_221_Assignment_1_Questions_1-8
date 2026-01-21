# Assignment 1, Question 8
# Joseph Krosel

# Importing pandas
import pandas as pd

# Global variable for data frame creation
dataOfNumbers = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

# Creating data frame
dataFrameOfNumbers = pd.DataFrame(dataOfNumbers)

# Adding a column
dataFrameOfNumbers["D"] = [-1, -2, -2, -1]

# Printing the data frame
print(dataFrameOfNumbers)