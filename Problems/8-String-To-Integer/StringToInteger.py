class Solution:
    def myAtoi(self, s):
        length = len(s)
        counting = False
        output = ""
        if s.isdigit():
            return int(s)
        
        for i in range(0, length):
            if not s[i].isdigit():
                if s[i] == " ":
                    continue
                if (s[i] == "-" or s[i] == "+") and counting == False:
                    counting = True
                    output += s[i]
                    continue
                break
                
            output += s[i]
        
        if output == "" or output == "+" or output == "-":
            return 0

        return max(min(int(output), 2147483647), -2147483648)