from typing import List, Optional


def majority_element(nums: List[int]) -> Optional[int]:
    nums_len: int = len(nums)
    if not nums_len:
        return None
    nums.sort()
    prev_num: int = nums[0]
    count: int = 1
    if nums_len == 1:
        return prev_num
    for i in range(1, nums_len):
        if nums[i] == prev_num:
            count += 1
            if count > nums_len // 2:
                return nums[i]
        else:
            prev_num = nums[i]
            count = 1
    return None
