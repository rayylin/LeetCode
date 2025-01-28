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


if __name__ == "__main__":
    
    target = 12
    l = [5,7,9]

    print(twoSum1(l, target))
    print(twoSum2(l, target))

