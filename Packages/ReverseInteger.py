class Solution:
    def reverse(self, x):
        if x > 0:
            x = int(str(x)[::-1])
        if x < 0:
            x = int(str(x*-1)[::-1]) * -1
        return x if x < 2**31 and x > -2**31 else 0