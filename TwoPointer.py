
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


# 15 three sum

def threeSum(nums:[int]) -> [int]:
    res = []
    nums.sort()

    for i, n in enumerate(nums):  # do not use repeated number: [-2, -2, -2, 0, 0, 0, 2, 2, 4]
        if i > 0 and n == nums[i-1]:
            continue

        l, r = i + 1, len(nums) -1 # 

        while l < r:
            thrSum = n + nums[l] + nums[r]

            if (thrSum > 0):
                r -= 1
            elif (thrSum < 0):
                l += 1
            else:
                res.append([n, nums[l], nums[r]])
                l += 1

                while (nums[l] == nums[l-1] and l < r):
                    l += 1
    return res

print(threeSum([-2,-2,-2,0,0,0,2,2,4]))