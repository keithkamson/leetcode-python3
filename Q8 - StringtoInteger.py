class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0: return 0

        num = 0
        step = 0
        sign = 1

        if s[0] == "-":
            sign = -1

        for i in s:
            if i.isnumeric():
                num = num*10 + int(i)
                step = 1
            elif (i == "+" or i == "-") and (step == 0):
                step = 1
                pass  
            else: break      
        
        num = num*sign

        if (-2**31<=num<=(2**31)-1): return num
        if num<0: return -2**31
        else: return 2**31-1

        
