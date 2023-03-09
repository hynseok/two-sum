def twoSum(self, nums: List[int], target: int) -> List[int]:
    result = []
    for i in range(len(nums)):
        for j in range(len(nums)) :
            if i==j: continue
            if nums[i]+nums[j]==target: 
                result.insert(0, i-1)
                result.insert(1, j-1)
                return result
    return


