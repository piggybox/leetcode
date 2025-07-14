class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        char_index_map = {}

        # sliding window pointers
        left = 0
        for right in range(len(s)):
            if s[right] in char_index_map:
                # Move the left pointer to the right of the last occurrence of s[right]!
                left = max(left, char_index_map[s[right]] + 1)
            
            # Update the last seen index of the character
            char_index_map[s[right]] = right
            
            # Calculate the length of the current substring
            longest = max(longest, right - left + 1)

        return longest