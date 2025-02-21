def lengthOfLongestSubstring( s: str) -> int:
    l, maxx = 0, 0
    exist = set()
    
    for r in range(len(s)):
        while(s[r] in exist):
            exist.remove(s[l])
            l += 1

        exist.add(s[r])
        maxx = max(r - l + 1, maxx)

    return maxx


def lengthOfLongestSubstring2( s: str) -> int:
    l, maxx = 0, 0
    exist = {}
    
    for r in range(len(s)):          # a substring cannot be longer than original string
        while(s[r] in exist):        # if a new char exists, pop from left until the char is removed. a char can exist at most once
            exist.pop(s[l])
            l += 1

        exist[s[r]] = 1
        maxx = max(r - l + 1, maxx)

    return maxx



print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring2("pwwkew"))







