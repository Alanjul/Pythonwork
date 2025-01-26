from typing import List
from typing import Optional
def second_max(nums: List[int]) -> Optional[int]:
    # TODO: Find the second largest number in nums
    if (len(nums) < 2):
        return None
    largest = nums[0]
    second = None
    for i in range(1,len(nums)):
        if(nums[i] > largest):
            second = largest
            largest = nums[i]
        elif(second is None or nums[i] > second  and nums[i] != largest):
            second = nums[i]
    return second
nums = [4,5,2,1]
print(second_max(nums))