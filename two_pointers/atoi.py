def myAtoi(s):
    sign = 1
    i = 0  # pointers
    result = 0
    num_chars = list(map(lambda x: str(x), range(0, 10)))

    # skip white space
    while i < len(s) and s[i] == " ":
        i += 1
    # process +/- symbols
    while i < len(s) and (s[i] == "+" or s[i] == "-"):
        if s[i] == "-":
            sign = -1
        i += 1

    while i < len(s):
        if s[i] not in num_chars:  # non-numeric
            break
        elif s[i] in num_chars:
            result = result * 10 + int(s[i])
            i += 1

    if result * sign > 2**31 - 1:
        return 2**31 - 1
    elif result * sign < -(2**31):
        return -(2**31)
    return result * sign
