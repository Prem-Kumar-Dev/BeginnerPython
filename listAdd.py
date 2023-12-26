class Solution:

    def addTwoNumbers(self,x,y):
        x="".join(str(i) for i in x)
        y="".join(str(j) for j in y)
        z=str(int(x)+int(y))
        z = list(map(int, z[::-1]))
        return z


solution=Solution()


param_1=[9,9,9,9,9,9,9]
param_2=[9,9,9,9]
res=solution.addTwoNumbers(param_1, param_2)
print(res)