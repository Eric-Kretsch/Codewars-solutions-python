# expressions matter
# Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ().

def expression_matter(a, b, c):
    max1 = (a + b) * c
    max2 = a * (b + c)
    max3 = a + b + c
    max4 = (a * b * c)
    listMax = [max1, max2, max3, max4]
    maxNumber = 0
    for i in listMax:
        if i > maxNumber:
            maxNumber = i
    return maxNumber