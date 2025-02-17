# two sum

def twoSum1(lst:[int], tar:int):
    for i in range(len(lst)-1):
        if tar - lst[i] in lst[i+1:]:
            return True 
    return False

def twoSum2(lst:[int], tar:int):
    dic = {}

    for i in lst:
        if i not in dic.keys():
            dic[tar-i] = 1
        else:
            return True
    return False

def GeneratePa(x:int):
    res = []
    def BT(l,r,s):
        if l == x and r == x:
            res.append(s)
        if l < x:
            BT(l+1, r, s + "(")
        if r < l:
            BT(l, r+1, s + ")")
    
    BT(0,0,"")
    return res



def permute(nums: [int]) -> [[int]]:
    res = []
    
    def BT(s):
        if len(s) == len(nums):
            res.append(s[:])  
            return
        
        for i in range(len(nums)):
            if nums[i] in s:
                continue  
            s.append(nums[i])
            BT(s)
            s.pop()  
            
    BT([])
    return res

def permute1(nums:[int]) -> [[int]]:
    res = []
    c = len(nums)

    def BackTrack(start):
        if (start == c):
            res.append(nums.copy())
            return

        for i in range(start, c):
            nums[i], nums[start] = nums[start], nums[i]
            BackTrack(start+1)
            nums[i], nums[start] = nums[start], nums[i]

    BackTrack(0)
    return res



def cumsum(cans:[int], target:int):
    res = []
    def dfs(i:int, cur:[int], total:int):
        if total == target:
            res.append(cur.copy())
            return 
        if i >= len(cans) or total >= target:
            return
        cur.append(cans[i])
        # print(cur)
        dfs(i, cur, total + cans[i])
        cur.pop()
        dfs(i+1, cur, total)

        
    
    dfs(0,[],0)
    return res

    
def cb(n:int, t:int):
    res = []
    
    def BT(start, comb):
        if (len(comb) == t):
            res.append(comb.copy())
            return
        
        for i in range(start, n+1):
            comb.append(i)
            BT(i+1, comb)
            comb.pop()
    BT(1,[])
    return res

def subset(nums:[int])->[int]:
    res = []
    sub = []

    def BackTrack(i:int):
        if i >= len(nums):
            res.append(sub.copy())
            return

        
        sub.append(nums[i])
        BackTrack(i+1)
        sub.pop()
        BackTrack(i+1)
    
    BackTrack(0)
    return res

def summaryRange(nums:[int]):
    range = []

    for i in nums:
        if range and range[-1][1] == i-1:
            range[-1][1] = i
        else:
            range.append([i,i])
    
    return [i[0] if i[0] == i[1] else [i[0],i[1]] for i in range] 


# Two Pointer
from TwoPointer import cw, twoSum2

def jg2_55(nums:[int])-> bool:
    mx = nums[0]

    for i in range(len(nums)):
        if i > mx: # max distance cannot reach a point in the list
            return False 
        elif i + nums[i] > mx:
            mx = i + nums[i] # set new max distance if reaching a new point
    return True if mx > len(nums) else False




if __name__ == "__main__":
    
    target = 12
    l = [5,7,9]

    print(twoSum1(l, target))
    print(twoSum2(l, target))

    print(GeneratePa(3))

    print(permute([1,2,3]))
    print(permute1([1,2,3]))

    print(cumsum([2,3,6,7], 7))
    print(cb(4,2))

    print(subset([1,2,3]))

    print(summaryRange([1,2,3,4,5,6,8,10]))


    print(jg2_55([2,3,1,1,4]))

    print(cw([1,8,6,2,5,4,8,3,7]))
    print(twoSum2([1,2,3,5,6,7,9,14], 13))

          
