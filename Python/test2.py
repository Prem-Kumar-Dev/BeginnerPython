class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ch=""
        c=1
        i=0
        while True:
           if c==1:
               if strs[0][i]==str[0][i]