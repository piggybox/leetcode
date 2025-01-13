from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sorted_arr = sorted(arr)
        result = []
        min_abs_diff = abs(sorted_arr[0] - sorted_arr[1])

        for i in range(len(sorted_arr) - 1):
            abs_diff = abs(sorted_arr[i] - sorted_arr[i + 1])
            
            if abs_diff < min_abs_diff:
                # reset result
                result = [[sorted_arr[i], sorted_arr[i + 1]]]
                min_abs_diff = abs_diff
            elif abs_diff == min_abs_diff:
                result.append([sorted_arr[i], sorted_arr[i + 1]])
            
        return result
