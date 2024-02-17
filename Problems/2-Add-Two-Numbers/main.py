from ListNode import ListNode
from AddTwoNumbers import Solution

if __name__ == "__main__":
    solution = Solution()
    keepLooping = True
    outputList = []
    
    l1 = ListNode(2, ListNode(4, ListNode(3, None)))
    l2 = ListNode(5, ListNode(6, ListNode(4, None)))
    output = solution.addTwoNumbers(l1, l2)

    while keepLooping:
        outputList.append(output.val)
        output = output.next
        if output == None:
            keepLooping = False
    
    print(outputList)