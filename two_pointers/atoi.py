def myAtoi(s):
    s = s.strip()  # remove white space

    sign = 1
    i, j = 0, 0  # pointers
    i_flag = True
    result = 0

    num_chars = list(map(lambda x: str(x), range(0, 10)))

    while i_flag:
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1
        elif s[i] not in num_chars:  # non-numeric
            return 0
        elif s[i] in num_chars:
            i_flag = False  # stop moving pointer i
            result += int(s[i])
            j = i + 1
            while j < len(s) and s[j] in num_chars:
                result = result * 10 + int(s[j])
                j += 1

    if result * sign > 2**31 - 1:
        return 2**31 - 1
    elif result * sign < -2**31:
        return -2**31  
    return result * sign
