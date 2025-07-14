class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_map = {0: -1} # position of the first occurrence of each count
        max_length = 0
        count = 0

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1 # Increment for 1, decrement for 0!
            
            if count in count_map:
                max_length = max(max_length, i - count_map[count])
            else:
                count_map[count] = i
        
        return max_length