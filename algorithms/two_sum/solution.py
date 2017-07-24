class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for ind, val in enumerate(nums):
            for ind2, val2 in enumerate(nums):
                if val + val2 == target and ind != ind2:
                    return (ind, ind2)
        raise ValueError('No two sums exist!')


if __name__ == '__main__':
    sol = Solution()
    print sol.twoSum([1, 2, 3, 4, 5], 3)
