import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        # print(len(cleaned_string))
        left, right = 0, len(cleaned_string) - 1
        # print(left, right)
        
        while left < right:
            if cleaned_string[left] == cleaned_string[right]:
               left += 1
               right -= 1
            else:
                return False
        return True
        