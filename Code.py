# two sum

def twoSum1(lst:[int], tar:int):
    for i in range(len(lst)-1):
        if tar - lst[i] in lst[i+1:]:
            return True 
    return False


if __name__ == "__main__":
    
    target = 12
    l = [6,6,9]

    print(twoSum1(l, target))

