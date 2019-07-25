HashSet <ListNode> meet = new HashSet();
while (headA != null || headB != null) {
    if (headA != null) {
        System.out.println("adding " + headA.val + meet.add(headA));
        if(!meet.add(headA)) return headA;
        headA = headA.next;
    }
    if (headB != null) {
        System.out.println("adding " + headB.val + meet.add(headB));
        if (!meet.add(headB)) return headB;
        headB = headB.next;
    }
}
return null;
}
