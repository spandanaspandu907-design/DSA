class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)
        ans = -1

        for i in range(n - k + 1):
            window = nums[i:i+k]

            for x in window:
                count = 0

                for j in range(n - k + 1):
                    if x in nums[j:j+k]:
                        count += 1

                if count == 1:
                    ans = max(ans, x)

        return ans