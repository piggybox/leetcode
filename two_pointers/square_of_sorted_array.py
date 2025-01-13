from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # scan from two ends
        result = []
        left, right = 0, len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1

        return result[::-1]  # also can use deque and appendleft
