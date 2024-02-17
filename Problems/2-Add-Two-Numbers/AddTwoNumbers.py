from ListNode import ListNode

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        output = []
        blank = ListNode()
        listNode = ListNode()          

        while l1.next != None or l2.next != None or carry != 0:
            num1 = 0 if l1 == None else l1.val
            num2 = 0 if l2 == None else l2.val
            total = num1 + num2 + carry
            if total >= 10:
                carry = 1
                total = total - 10
            else: 
                carry = 0

            output.append(total)
            l1 = l1.next if l1.next != None else blank
            l2 = l2.next if l2.next != None else blank
        
        if l1.next == None and l2.next == None and (l1.val != 0 or l2.val != 0):
            total = l1.val + l2.val
            if total >= 10:
                carry = 1
                total = total - 10
                output.append(total)
                output.append(carry)
            else:
                output.append(total)

        output.reverse()

        for i in range(0, len(output)):
            if i == 0:
                listNode = ListNode(output[i], None)
            else:
                listNode = ListNode(output[i], listNode)

        return listNode
        
        

