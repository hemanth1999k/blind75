class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        new_x = str_x[::-1]

        if str_x == new_x:
            return True
        else:
            return False    


        