# Assignment 1, Question 3
# Joseph Krosel

pairs = [[5, 2], [3, -1], [4, 3], [2, 0]]
storedList = []
for x, y in pairs:
    if y < 0:
        continue
    storedList.append(x**y)
print(storedList)