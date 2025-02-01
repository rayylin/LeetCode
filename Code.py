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

    






if __name__ == "__main__":
    
    target = 12
    l = [5,7,9]

    print(twoSum1(l, target))
    print(twoSum2(l, target))

    print(GeneratePa(3))

    print(permute([1,2,3]))

    print(cumsum([2,3,6,7], 7))