# Given two binary strings str1 and str2, return their sum as a binary string.


def add_binary(str1: str, str2: str) -> str:
    result = ""
    carry = 0

    # retrieve digits reversely
    p1, p2 = len(str1) - 1, len(str2) - 1

    # iterate through two strings
    while p1 >= 0 or p2 >= 0:
        # retrieve current digit from two strings
        if p1 < 0:
            num_1 = 0
        else:
            num_1 = int(str1[p1])

        if p2 < 0:
            num_2 = 0
        else:
            num_2 = int(str2[p2])

        # summing logic
        if num_1 + num_2 + carry == 0:
            result += "0"
            carry = 0
        elif num_1 + num_2 + carry == 1:
            result += "1"
            carry = 0
        elif num_1 + num_2 + carry == 2:
            result += "0"
            carry = 1
        elif num_1 + num_2 + carry == 3:
            result += "1"
            carry = 1

        # move pointers
        p1 -= 1
        p2 -= 1

    # handle final carry
    if carry == 1:
        result += "1"

    return result[::-1]
