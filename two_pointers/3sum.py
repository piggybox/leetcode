from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # transform the given input to a more useful data structure
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # skip already evaluated
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # two pointers scan from two sides
            left = i + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # continue finding more results
                    left += 1
                    right -= 1
                    # skip duplicated solution
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result
