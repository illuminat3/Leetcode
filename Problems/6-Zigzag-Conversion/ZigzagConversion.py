class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        output = ""
        length = len(s)
        interval = 2 * (numRows - 1)

        for row in range(numRows):
            step = row
            isFirst = True
            while step < length:
                output += s[step]
                if row == 0 or row == numRows - 1:
                    increase = interval
                else:
                    if isFirst:
                        increase = 2 * (numRows - 1 - row)
                        isFirst = False
                    else:
                        increase = interval - increase
                step += increase

        return output

       