class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

x = int(input())

p1 = Solution()
ans = p1.isPalindrome(x)
print(ans)




