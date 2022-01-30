# LeetCode-Practice
<div class="text-white bg-blue mb-2">
  .text-white on .bg-blue
</div>
First we define the pointers:
    dummy = pre = ListNode(0)
    dummy.next = head

There is two conditions:
1. The next variable is same the previous one:
    if head.val == head.next.val:
2. The next variable is different from the preivous one:
    