def twoSum(self, nums: List[int], target: int) -> List[int]:
    result = []
    for i in range(len(nums)):
        for j in range(len(nums)) :
            if i-1==j-1: continue
            if nums[i-1]+nums[j-1]==target: 
                result.insert(0, i-1)
                result.insert(1, j-1)
                return result
    return


