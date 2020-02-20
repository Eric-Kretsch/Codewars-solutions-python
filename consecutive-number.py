#Your task is to find the first element of an array that is not consecutive.

#E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.

#If the whole array is consecutive then return null2.

def first_non_consecutive(arr):
    consecutiveNumber = arr[0]
    for i in arr[1:]:
        if i == consecutiveNumber + 1:
            consecutiveNumber = i
        elif i != consecutiveNumber + 1:
              return i
        else:
            return 'null'