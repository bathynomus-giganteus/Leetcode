def isAnagram(self, s: str, t: str) -> bool:
    i = True
    if len(s) != len(t):
        i = False
    if s == t:
        i = 's and t are the same string'
    for each in set(t):
        if t.count(each) != s.count(each):
            i = False
    return i
self = 1
s = "anagram"
t = "nagaram"
print(isAnagram(self, s, t))
s = "一二三"
t = "一二四"
print(isAnagram(self, s, t))