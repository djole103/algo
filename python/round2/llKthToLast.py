#return Kth last node

def KthLast(head, k):
        kth, kahead = head, head
        for i in range(k):
                kahead = kahead.next
        while(kahead != None):
                kth = kth.next
                kahead = kahead.next
        return kahead
