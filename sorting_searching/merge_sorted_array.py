# easy


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        

        j = 0  # pointer for nums2
        for i in range(m):
            if j > n - 1:
                break
            if nums1[i] < nums2[j]:
                continue  # i += 1
            else:
                # shift the remaining of nums
                for k in range(len(nums1) - 1, i, -1):
                    nums1[k] = nums1[k - 1]
                # insert nums2[j] into nums1
                nums1[i] = nums2[j]
                j += 1

        # continue the rest of nums2
        if j < n - 1:
            for k in range(j, n):
                nums1[m + k] = nums2[k]
