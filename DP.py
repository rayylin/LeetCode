def targetSum494(nums:[int], tar:int):
    resDic = {}

    def DP(index:int, total: int):
        if (index == len(nums)):
            return 1 if total == tar else 0 # return 1 if match
        
        if ((index, total) in resDic):
            return resDic[(index, total)]
        
        resDic[(index, total)] = (DP(index+1, total + nums[index])
                               +  DP(index+1, total - nums[index]))
        return resDic[index, total]
    return DP(0, 0)

print(targetSum494([1,1,1,1,1], 3))