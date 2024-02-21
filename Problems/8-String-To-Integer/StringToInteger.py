class Solution:
    def myAtoi(self, s):
        length = len(s)
        counting = False
        output = ""
        if s.isdigit():
            return int(s)
        
        for i in range(0, length):
            if not s[i].isdigit():
                if counting:
                    break
                if s[i] == "-" or s[i] == "+":
                    output += s[i]
                    counting = True
                    continue
                continue
            output += s[i]
            counting = True
        
        if output == "":
            return 0

        return max(min(int(output), 2147483647), -2147483648)