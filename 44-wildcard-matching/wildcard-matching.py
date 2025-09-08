class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        prev = [False] * (m + 1)
        prev[0] = True
        for j in range(1, m + 1):
            prev[j] = prev[j - 1] and p[j - 1] == '*'
        for i in range(1, n + 1):
            curr = [False] * (m + 1)
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    curr[j] = curr[j - 1] or prev[j]
                else:
                    curr[j] = prev[j - 1] and (p[j - 1] == '?' or p[j - 1] == s[i - 1])
            prev = curr
        return prev[m]