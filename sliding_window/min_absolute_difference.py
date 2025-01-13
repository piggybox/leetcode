from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        min_abs_diff = abs(arr[0] - arr[1])

        for i in range(len(arr) - 1):
            abs_diff = abs(arr[i] - arr[i + 1])
            
            if abs_diff < min_abs_diff:
                # reset result
                result = [[arr[i], arr[i + 1]]]
                min_abs_diff = abs_diff
            elif abs_diff == min_abs_diff:
                result.append([arr[i], arr[i + 1]])
            
        return result
