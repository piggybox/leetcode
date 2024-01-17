# medium


def find_sum_of_three(nums, target):
    sorted_nums = sorted(nums)

    for mid in range(1, len(sorted_nums) - 1):  # position 1 to n-1
        left, right = 0, len(nums) - 1
        while left < mid and right > mid:
            sum = sorted_nums[left] + sorted_nums[mid] + sorted_nums[right]
            if sum == target:
                return True
            elif sum > target:
                right -= 1
            else:
                left += 1

    return False
