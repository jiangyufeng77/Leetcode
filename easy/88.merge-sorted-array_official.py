class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ## solution1: 先合并后排序
        # nums1[:] = sorted(nums1[:m]+nums2[:n])
        # return nums1

        ## solution2： 双指针，从后向前比较
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1

        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        # add missing elements from nums2
        # 将nums2中小于nums1[0]的值全部赋值到nums2的前面
        nums1[:p2 + 1] = nums2[:p2 + 1]
        return nums1

solution = Solution()
nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1
results = solution.merge(nums1, m, nums2, n)
print(results)

# 耗时很长，执行用时为40ms，打败8.39%的用户
# 占用的内存也多，内存消耗11.8MB，击败了15.51%的用户