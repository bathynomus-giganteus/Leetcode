class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not len(s):
            return t
        s = list(s)
        t = list(t)
        while s:
            for i in range(len(t)):
                if s[0] == t[i]:
                    t.pop(i)
                    s.pop(0)
                    break
        return t[0]
    self = 0
    s = input('请输入对照字符串： ')
    t = input('请输入要检查的字符串： ')
    print(findTheDifference(self, s, t))