class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        for i in range(len(a)):
            if a[i] == a[::-i]:
                return True
            else:
                False