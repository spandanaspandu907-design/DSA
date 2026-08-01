def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        difference = target - nums[i]

        if difference in seen:
            return [seen[difference], i]

        seen[nums[i]] = i

    return []

# Example
nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print(result)