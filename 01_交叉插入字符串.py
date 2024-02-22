class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if isinstance (word1,str) is False or isinstance (word2,str) is False:
            raise TypeError('invalid input format')
        w1 = list(word1)
        w2 = list(word2)
        i = 1
        if len(w1) > len(w2):
            for i in range (len(w1) - len(w2)):
                w2.append('')
                i += 1
        elif len(w2) > len(w1):
            for i in range(len(w2) - len(w1)):
                w1.append('')
                i += 1
        i = 0
        merge = [ w1[i] + w2[i] for i in range(len(w1))]
        return ''.join(merge)
    self = 0
    word1 = input('请输入第一个字符串： ')
    word2 = input('请输入第二个字符串： ')
    print (mergeAlternately(self, word1, word2))