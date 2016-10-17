romanD = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

num_to_roman(c, digit):
    if digit == 1:
        return romanD[c]
    if digit == 9:
        return romanD[c*10] + romanD[c]
    if digit == 5:
        return romanD[c * 5]
    if digit > 5:
        return romanD[c] * (digit % 5) + romanD[c * 5]
    if digit == 4:
        return romanD[c * 5] + romanD[c]
    # digit < 4
    return digit * romanD[c]
        

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        n = num
        c = 1
        roman = ""
        while(n != 0):
            digit = n%10
            roman += num_to_roman(c, digit)
            n = n // 10
            c = c*10
        return roman[::-1]
