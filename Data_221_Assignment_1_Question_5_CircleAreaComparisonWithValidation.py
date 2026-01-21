# Assignment 1, Question 5
# Joseph Krosel
import math

# Definiting the function
def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    if radiusOfCircle1 > 0 and radiusOfCircle2 > 0:
        # Calculates the area
        areaOfCircle1 = math.pi * (radiusOfCircle1 ** 2)
        areaOfCircle2 = math.pi * (radiusOfCircle2 ** 2)

        # Calculating the larger circle and the area covered bu the smaller circle
        if (areaOfCircle2 > areaOfCircle1):
            areaCoveredBySmallCircle = areaOfCircle1 / areaOfCircle2
        else:
            areaCoveredBySmallCircle = areaOfCircle2 / areaOfCircle1

        # Prints the result
        print(areaCoveredBySmallCircle)