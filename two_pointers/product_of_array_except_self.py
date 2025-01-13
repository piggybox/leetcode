# medium


def product_except_self(nums):
    res = [1] * len(nums)  # initialize an array of 1
    l, r = 0, len(nums) - 1
    prod_l, prod_r = 1, 1

    while l < len(nums):
        res[l] *= prod_l
        res[r] *= prod_r

        prod_l *= nums[l]
        prod_r *= nums[r]

        l += 1
        r -= 1

    return res
