# Name: Jamar Hill
# Date: 5/10/2021
# Description: CS 162 Project 6b

# Recursive functions
# 1. Base case -> The most basic form of the question broken down
# 2. If not base, what can we do to break the problem down
# 3. Recursively call the function with the smaller problem

# lst = [5, 6, 10, 9, 8, 7, 64, 10]
#               ^                ^
def is_decreasing(list):
    return is_decreasing_helper(list, 0, len(list) - 1)  # passed in the beginning index and ending index


def is_decreasing_helper(list, fstPos, lstPos):
    if fstPos < lstPos:
        if list[fstPos] >= list[fstPos + 1]:
            return is_decreasing_helper(list, fstPos + 1, lstPos)  # Recursive call, and also update fstPos
        else:
            return False
    else:
        return True

print(is_decreasing([9, 6, 3, 1]))

