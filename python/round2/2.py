from collections import defaultdict

N = int(raw_input())
tally = defaultdict(int)
winners = []
maxvotes = 0
for i in range(N):
        vote = raw_input()
        tally[vote] += 1
        if tally[vote] == maxvotes:
                winners.append(vote)
        elif tally[vote] > maxvotes:
                winners = [vote]
                maxvotes = tally[vote]
if len(winners) > 1:
        print(max(winners))
else:
        print(winners[0])

