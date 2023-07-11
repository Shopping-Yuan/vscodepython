class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        while i+1< len(nums):
            j = i+1
            while j< len(nums):
                if nums[i]+nums[j]==target:
                    return [i,j]
                    break
                j+=1
            i+=1