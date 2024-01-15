class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Replace this placeholder return statement with your code
        result = 0
        left, right = 0, len(height) - 1

        while left < right:
            current = min(height[left], height[right]) * (right - left)
            if current > result:
                result = current

            # move the smaller needle
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return result
