class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_target_element(head: ListNode):
    n = 0
    curr = head
    while curr is not None:
        n += 1
        curr = curr.next
    if n <= 1:
        return None

    target_pos = (2 * n) // 3 - 1
    curr = head
    for _ in range(target_pos):
        curr = curr.next

    return curr.val

#examples from task
# 1) 0 -> 1 -> 2, n = 3
head1 = ListNode(0, ListNode(1, ListNode(2)))
print(f"Приклад 1: {find_target_element(head1)}")
# 2) 0 -> 1 -> 2 -> 3, n = 4
head2 = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
print(f"Приклад 2: {find_target_element(head2)}")
# 3) 0 -> 1 -> 2 -> 3 -> 4, n = 5
head3 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
print(f"Приклад 3: {find_target_element(head3)}")