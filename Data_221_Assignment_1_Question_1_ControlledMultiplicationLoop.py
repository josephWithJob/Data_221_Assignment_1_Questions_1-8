# Assignment 1, Question 1
# Joseph Krosel

threshold = 100
product = 1
currentNumber = 1

while product < threshold:
    product = product * currentNumber
    currentNumber += 1

print(f"Final product: {product}. Current number: {currentNumber}")