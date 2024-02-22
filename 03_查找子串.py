def strStr(self, haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
        i = -1
        return i
    k = 0
    for i in range(len(haystack)):
        if needle[0] == haystack[i] and len(needle) <= (len(haystack) - i):
            for j in range(len(needle)):
                if needle[j] != haystack[i+j]:
                    k = 0
                    break
                else:
                    k = 1
        if k == 1:
            break
    if k == 0:
        i = -1
    return i

self = 0    
haystack = 'sadbutsad'
needle = 'sad'
print(strStr(self, haystack, needle))
haystack = 'leetcode'
needle = 'leeto'
print(strStr(self, haystack, needle))
haystack = ''
needle = 'leeto'
print(strStr(self, haystack, needle))