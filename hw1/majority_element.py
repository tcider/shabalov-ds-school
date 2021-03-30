class Solution:
    def majority_element(self, nums: List[int]) -> int:
        nums.sort()
        prev_num = nums[0]
        count = 1
        nums_len = len(nums)
        if nums_len == 1:
            return prev_num
        for i in range (1, nums_len):
            if nums[i] == prev_num:
                count += 1
                if count > nums_len // 2:
                    return nums[i]
            else:
                prev_num = nums[i]
                count = 1;
