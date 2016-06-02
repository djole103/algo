from collections import defaultdict
import heapq

#word to doc ids
reverseIndex = {"word" : [1,2,3],
                "what" : [2,5],
                "is"   : [1,2,4]}

def relevantPages(query):
        d = defaultdict(int)
        for word in query:
                for docID in reverseIndex[word]:
                        d[docID] += 1
        return d

def rankTop3(d):
        top3 = []
        while(len(top3) < 3 and d):
                docID, score = d.popitem()
                top3.append([score, docID])
        heapq.heapify(top3)
        while(d):
                docID, score = d.popitem()
                if score < top3[0][1]:
                        heapq.heappushpop(top3, [score, docID])
        return top3

def parse(s):
        words = s.split(" ")
        return words

QUERY = "what is word"
words = parse(QUERY)
pages = relevantPages(words)
top3 = sorted(rankTop3(pages), reverse = True)
print(top3)



