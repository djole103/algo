#NOT DONE, this problems stupid
from collections import defaultdict

def buildPlan(l):
        dependsOn = defaultdict(list)
        preceeds = defaultdict(list)
        tasks = set()
        for d in l:
                if d[0] not in tasks:
                        tasks.add(d[0])
                if d[1] not in tasks:
                        tasks.add(d[1])
                dependsOn[d[1]].append(d[0])
                preceeds[d[0]].append(d[1])
        if len(dependsOn.keys()) > len(tasks) - 1:
                return False
        result = []
        while(tasks):
                for t in tasks:
                        if t not in dependsOn:
                                result.append(t)
                                
                                tasks.remove(t)
                                break
        return results

TEST1 = [[1, 2], [1,3], [2,4]]
TEST2 = [[1,2], [2,3], [3,1]]

print(buildPlan(TEST1))
print(buildPlan(TEST2))

