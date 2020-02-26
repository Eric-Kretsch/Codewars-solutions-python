#Given an array, find the integer that appears an odd number of times.
#There will always be only one integer that appears an odd number of times.

def find_it(seq):
    nums = {}
    for i in seq:
        if i in nums:
            nums[i] += 1
        else:
            nums[i] = 1
    for key in nums:
        if nums[key] % 2 == 0:
            pass
        else:
            solution = key
    return solution
