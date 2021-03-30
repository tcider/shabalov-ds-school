class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        tmp_sum = 0
        max_sum = nums[0]
        for elem in nums:
            tmp_sum += elem
            if tmp_sum > max_sum:
                max_sum = tmp_sum
            if tmp_sum < 0:
                tmp_sum = 0
        return max_sum
