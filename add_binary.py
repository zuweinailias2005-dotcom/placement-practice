a = "11"
b = "1"

class Solution(object):
    def addBinary(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ""

        while i >= 0 or j >= 0 or carry:
            digit1 = int (a[i]) if i >= 0 else 0
            digit2 = int (b[j]) if j >= 0 else 0

            total = digit1 + digit2 + carry

            result += str(total % 2)
            carry = total // 2

            i -= 1
            j -= 1
        return result[::-1]
        
       
        