
#container With most water 11
def cw(nums:[int]):
    mx = 0
    l, r = 0, len(nums)-1

    while (l<r):
        area = (r-l) * min(nums[l], nums[r])
        if area > mx:
            mx = area

        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1 
    return mx


# 167
def twoSum2(nums:[int], tar:int)->[int]:
    l, r = 0, len(nums)-1

    while(l < r):
        curSum = nums[l] + nums[r]
        if (curSum > tar):
            r -= 1
        elif (curSum < tar):
            l += 1
        else:
            return [l+1, r+1]
    return []


