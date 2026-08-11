class Solution:
    def pivotIndex(self, nums):
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - left - nums[i]

            if left == right:
                return i

            left += nums[i]

        return -1
s = Solution()
print(s.pivotIndex([1, 7, 3, 6, 5, 6]))
print("Testing")