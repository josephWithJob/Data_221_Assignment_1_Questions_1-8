# Assignment 1, Question 2
# Joseph Krosel

# Defines the function
def time_checker(secondsSinceMidnight):
    # Checks if the seconds are in the correct rang
    if -1 < secondsSinceMidnight < 86400:
        # Calculates the hours, minutes and seconds
        hoursSinceMidnight = secondsSinceMidnight // 3600
        minutesSinceMidnight = (secondsSinceMidnight % 3600) // 60
        secondsSinceMidnight = secondsSinceMidnight % 60

        # Calculates the AM or PM
        periodOfTime = ""
        if hoursSinceMidnight < 12:
            periodOfTime = "AM"
        else:
            periodOfTime = "PM"

        # If hours are zero, it would be midnight
        if hoursSinceMidnight == 0:
            hours = 12

        # Returns the data in the correct string format
        return (f"{hoursSinceMidnight}:{minutesSinceMidnight}:{secondsSinceMidnight} {periodOfTime}")
    else:
        # If the wrong range is input. Respond with a error message
        return "Invalid Input"