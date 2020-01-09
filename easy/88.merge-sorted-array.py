class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        count = 0
        if n == 0: return nums1
        for i in range(len(nums1)):
            if i < m + j and j < n:
                if nums1[i] >= nums2[j]:
                    nums1.insert(i, nums2[j])
                    count += 1
                    j += 1
            elif i == m + j:
                if j <= n:
                    nums1[i] = nums2[j]
                    j += 1
        for c in range(count):
            del nums1[-1]

        return nums1

solution = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
results = solution.merge(nums1, m, nums2, n)
print(results)

# 耗时很长，执行用时为40ms，打败8.39%的用户
# 占用的内存也多，内存消耗11.8MB，击败了15.51%的用户