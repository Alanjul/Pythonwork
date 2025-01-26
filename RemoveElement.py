from typing import  List
def remove(nums: List[int]) :
    k = 0
    #loop through the elements
    for i in range(len(nums)):
        #find numbers not repeating
        if nums[i] != nums[k]:
            nums[k] = nums[i]
            k+=1 #move to the next number

    return k #length of modified elements
nums = [1,2,2,4,5,4]
print(remove(nums))
