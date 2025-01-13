# shuffle an array
# medium

from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.list = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.list

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        import random

        return random.sample(self.list, len(self.list))


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
