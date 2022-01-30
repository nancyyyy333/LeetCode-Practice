class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        a , b = [] , []
        for i in s:
            #a[:-1] is for removinglast character
            a = a + [i] if i != '#' else a[:-1]
        for j in t:
            b = b + [j] if j != '#' else b[:-1]
        return a == b