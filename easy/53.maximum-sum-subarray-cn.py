class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        minsum = sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            maxsum = max(maxsum, sum - minsum)
            minsum = min(sum, minsum)

        return maxsum

solution = Solution()
a = [-2,1,-3,4,-1,2,1,-5,4]
results = solution.maxSubArray(a)
print(results)