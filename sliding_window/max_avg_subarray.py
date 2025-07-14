class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the sum of the first 'k' elements
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # Slide the window across the rest of the array
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)

        return max_sum / k