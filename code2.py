class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    p, q = l1, l2
    while p or q:
        x = p.val if p else 0
        y = q.val if q else 0
        s = x + y + carry
        carry = s // 10
        current.next = ListNode(s % 10)
        current = current.next

        if p:
            p = p.next
        if q:
            q = q.next

    if carry:
        current.next = ListNode(carry)

    return dummy.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


sum_list = addTwoNumbers(l1, l2)


while sum_list:
    print(sum_list.val, end=' ')
    sum_list = sum_list.next