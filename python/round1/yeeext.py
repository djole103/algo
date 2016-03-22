import math

def inttostr(num):
    if(num == 0) return '0'
    if num < 0: 
        negative = True
        num = abs(num)
    strdigits = "0123456789"
    string = ""
    while(num):
        digit = num % 10
        string = strdigits[digit] + string
        num = num // 10
    if negative: string = '-' + string
    return string

def findLCA(a,b):
    depthA = 0
    depthB = 0
    while(a.parent()):
        if a.parent() == b: return b
        depth+=1
    while(b.parent()):
        if b.parent() == a: return a
    if min(depthA,depthB) == a: 
        ancestorLower = a
        aLDepth = depthA
        ancestorHiger = b
        aHDepth = depthB
    else:
        ancestorLower = b
        aLDepth = depthB
        ancestorHiger = a
        aHDepth = depthA
    while(aLDepth!=aHDepth):
        ancestorLower = ancestorLower.parent()
        aLDepth-=1
    while(ancestorLower.parent() != ancestorHigher.parent()):
        ancestorLower = ancestorLower.parent()
        ancestorHigher = ancestorHigher.parent()
    return ancestorLower.parent()   
