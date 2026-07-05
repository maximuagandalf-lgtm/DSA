class Solution(object):
    def palindrome(self, x):
        str1 = str(x)
        str2 = str1[::-1]
        print(str1, str2)
        if str1 == str2:
            return True
        else:
            return False
    
    def romanToInt(self, s):
        numerals = {"I":1, "V":5, "X":10,"L":50, "C":100, "D":500, "M":1000}
        x = []
        j = 0
        num = 0
        l = 0
        for i in s:
                x.append(numerals[i])
        # while l<=len(x):
        #     if x[l]<x[l+1]:
        #         x[l] = x[l+1] - x[l]
        #         del x[l+1]
        #     else:
        #         pass
        #     l=l+1
            
        while j < len(x):
            num = num + x[j]
            j = j+1
        return num
        
            
#driver_code
s1 = Solution()
print(s1.palindrome(121))

print(s1.romanToInt("III"))
