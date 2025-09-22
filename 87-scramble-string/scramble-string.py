class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        if len(s1) == 1:
            return s1 == s2
        
        n = len(s1)
        dp = [[[False] * (n + 1) for _ in range(n)] for __ in range(n)]
        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i][j][1] = True
        
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                for j in range(n - l + 1):
                    for k in range(1, l):
                        if (dp[i][j][k] and dp[i + k][j + k][l - k]) or (dp[i][j + l - k][k] and dp[i + k][j][l - k]):
                            dp[i][j][l] = True
                            break
        return dp[0][0][n]