# fab 1 1 2 3 5 8 13 21
def fab1(tar:int): 
    
    if (tar <= 1):
        return 1
    else:
        return fab1(tar - 1) + fab1(tar - 2)
    
# 
def fab2(tar:int): # DP with caching
    dic = {0:1, 1:1}

    def rec(i):
        if i in dic:
            #print("used" + str(i))
            return dic[i]

        else:
            summ = rec(i - 1) + rec(i - 2)
            dic[i] = summ
            return summ
    return rec(tar)


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

print(fab1(10))
print(fab2(10))