import re
def solution(S):
    lines = re.findall(r"[^\.!\?]+(?=[\.!\?]+)", S)
    
    print([(line, len(line.split(' '))) for line in lines]) 
   #return max([len(line.split(' ')) for line in lines]) 

s = "We test coders. Give us a try?"
solution(s)
