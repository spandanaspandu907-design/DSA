def max_product(nums):
    nums.sort()

    n = len(nums)

    return (nums[n-1] - 1) * (nums[n-2] - 1)


# Example
nums = [3, 4, 5, 2]

result = max_product(nums)
print(result)