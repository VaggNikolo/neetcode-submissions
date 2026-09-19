class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=valid_char(s)
        rev = valid_char(s[::-1]).lower()
        print(rev)
        return s.lower() == rev

def valid_char(s: str)->str:
    res=''
    for c in s:
        if c.isalpha() or c.isdigit():
            res+=c
    return res