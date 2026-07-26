class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        letters = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        n=len(s)
        for i in range (0,n):
            if i<n-1 and letters[s[i]]<letters[s[i+1]]:
                res -= letters[s[i]]
            else:
                res += letters[s[i]]
        return res
        