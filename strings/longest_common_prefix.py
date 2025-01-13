from typing import List


class Solution:
    # lazy version using sort
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        strs.sort()
        p = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                p += x
            else:
                break

        return p

    # regular version
    def index_of(val, in_list):
        try:
            return in_list.index(val)
        except ValueError:
            return -1

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(len(strs)):
            while index_of(prefix, strs[i]) != 0:
                prefix = prefix[:-1]
                if len(prefix) == 0:
                    return ""
        return prefix
