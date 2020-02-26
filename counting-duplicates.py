#Count the number of Duplicates
#Write a function that will return the count of distinct case-insensitive alphabetic characters
# and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    dupDict = {}
    dupCount = 0
    for i in text.lower():
        if i in dupDict:
            dupDict[i] += 1
        else:
            dupDict[i] = 1
    for key in dupDict:
        if dupDict[key] > 1:
            dupCount += 1
    return dupCount