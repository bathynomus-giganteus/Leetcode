class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not len(s):
            return t
        for each in set(t):
            if t.count(each) != s.count(each):
                return each
    self = 0
    s = input('请输入对照字符串： ')
    t = input('请输入要检查的字符串： ')
    print(findTheDifference(self, s, t))