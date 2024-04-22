class Solution:
    def romanToInt(self, s: str) -> int:
        s=list(s)
        s=s[::-1]
        sum=0
        dic={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(0,len(s)):
            if i>0 and dic.get(s[i])<dic.get(s[i-1]):
                sum=sum-int(dic.get(s[i]))
            else:
                sum=sum+int(dic.get(s[i]))
        return sum

