class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0      # 考虑列表为空的情况
        t = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if t == nums[i]:
                nums.remove(nums[i])
            else:
                t = nums[i]
        return len(nums)

solution = Solution()
num = [0,0,1,1,1,2,3,3,4,4]
results = solution.removeDuplicates(num)
print(results)

# 这种方法如果不加考虑列表为空的情况会报错，但是加上后，运行时间和所占内存显著增加