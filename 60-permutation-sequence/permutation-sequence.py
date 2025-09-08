class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        ls = []
        for i in range(1,n):
            ls.append(i)
            fact*=i
        ls.append(n)
        ans = ""
        k-=1
        while True:
            temp = k//fact
            ans += str(ls[temp])
            ls.pop(temp)
            if len(ls)==0:
                break
            k = k%fact
            fact = fact // len(ls)
        return ans