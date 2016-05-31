def cycle(h):
        d = {h : True}
        n = h.next
        while(n != None and n not in d and n != h ):
                d[n] = True
                n = n.next
        return n != None

"""
Guaranteed cycle, do slow and fast runner where fast twice as fast
when slow has taken k steps to just enter cycle then fast runner will be 2k - k into cycle
once you're in cycle you're always catching up by 1
this means since it's cycleLength - k behind that's also where they'll meet
"""
deef meetCycle(h):
        slow = h
        fast = h
        while(fast != None and fast.next != None):
                slow = slow.next
                fast = fast.next.next
        if(fast == None or fast.next == None):
                return None
        while(h != slow):
                h = h.next
                slow = slow.next
        return h

