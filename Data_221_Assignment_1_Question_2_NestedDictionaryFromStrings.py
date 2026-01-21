# Assignment 1, Question 2
# Joseph Krosel

listOfStrings = ["Dog", "House", "Joseph"]

dictionaryOfStrings = {}
for i in listOfStrings:
    # Calculates the parity of the word
    parityOfWord = ""
    lengthOfWord = len(i)
    if lengthOfWord % 2 == 0:
        parityOfWord = "even"
    else:
        parityOfWord = "odd"

    dictionaryOfStrings[i] = {"length" : lengthOfWord, "parity" : parityOfWord}

print(dictionaryOfStrings)






