# Squash the bugs
# Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value. Output should be the length of the longest word, as a number.
# There will only be one 'longest' word.

def find_longest_str(string):
    list_string = list(string.split(" "))
    longest = 0
    for word in list_string:
        if len(word) > longest:
            longest = len(word)
    return longest

find_longest_str("this is a test beastmode")

