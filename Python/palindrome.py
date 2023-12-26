class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        y=y[::-1]
        return str(x)==y
    
        
solution=Solution()
x=121
res=solution.isPalindrome(x)
print(res)
