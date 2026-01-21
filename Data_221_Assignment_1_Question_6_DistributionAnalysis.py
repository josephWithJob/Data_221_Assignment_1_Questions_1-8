# Assignment 1, Question 6
# Joseph Krosel

numbers = [3, 1, 2, 3, 4, 2]

# Defines a function for distribution_analysis
def distribution_analysis(listOfNumbers):
    # Creates a dictionary
    resultingDictionary = {}

    # Removes duplicates and assignes values for resultingDictionary
    for i in sorted(set(listOfNumbers)):
        countOfNumbers = sum(1 for n in listOfNumbers if n <= i)
        resultingDictionary[i] = (countOfNumbers / len(listOfNumbers)) * 100

    # Returns data
    return resultingDictionary