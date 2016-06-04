import math

def whenLineCovered(line, rain = []):
        covered = []
        while(rain):
                drop = rain.pop()
                newCover = intersection(line, drop)
                newCover = sanitizeRng(newCover, line)
                covered = mergeRng(covered, newCover)
                if covered and covered[0] == line:
                        return "Covered"
        return "Not enough rain"

def sanitizeRng(rng, line):
        if not rng:
                return []
        if rng[0] < line[0] and rng[1] >= line[0]:
                rng[0] = line[0]
        if rng[1] > line[1] and rng[0] <= line[1]:
                rng[1] = line[1]
        return rng

def intersection(line, drop):
        """
        line = (x1, x2) we are assuming y = 0
        drop = (a,b) , x, y coordinates, just for naming

        line
        y = 0, x E [x1,x3]

        drop covers
        0.5**2 = (x-a)**2 + (y-b)**2

        intersecting
        0 = (x-a)**2 + (-b)**2 - 0.5**2
        """
        
        if  drop[1] < -0.5 or drop[1] > 0.5:
                return []
        if  drop[0] < min(line[0], line[1]) - 0.5 or drop[0] > max(line[0], line[1]) + 0.5:
                return []

        #set y=0 and intersect
        a = 1
        b = 2*(-drop[0])
        c = drop[0]**2 + drop[1]**2 - 0.5**2
        
        disc = b**2 - (4*a*c)
        if disc < 0:
                print("NEGATIVE DISCRIMINANT")
                return []
        r1 = (-b + math.sqrt(disc))/(2*a)
        r2 = (-b - math.sqrt(disc))/(2*a)

        rng = [min(r1, r2), max(r1, r2)]
        return rng

def mergeRng(covered, new):
        if not new:
                return covered
        result = []
        for i in range(len(covered)):
                if (new[0] > covered[i][1]):
                        result.append(covered[i])
                        continue
                if (new[1] < covered[i][0]):
                        result.append(new)
                        result += covered[i:]
                        return result
                if (new[0] <= covered[i][0]):
                        if (new[1] <= covered[i][1]):
                                new[1] = covered[i][1]
                                result.append(new)
                                result += covered[i+1:]
                                return result
                        if(new[1] > covered[i][1]):
                                continue
                #new start must be larger than curr covered start
                if (new[1] <= covered[i][1]):
                        #this range already covered
                        return covered
                if (new[1] > covered[i][1]):
                        new[0] = covered[i][0]
        result.append(new)
        return result
"""
TEST CASES
--------------------------
Covered
New

1.-----------------------

        [  ]
[ ]

newEnd < covStart

2.---------------------------

[ ]
    [ ]
newStart > covEnd

3.--------------------------

[  ]
  [   ]
newStart >= covStart
newEnd > covEnd

4.---------------------------

   [  ]
 [  ]
newStart <= covStart
newEnd <= covEnd

5.--------------------------

[    ]
 [  ]
newStart >= covStart
newEnd <= covEnd

6.--------------------------

  [ ]
[     ]
newStart <= covStart
newEnd >= covEnd

-----------------------
"""


T1 = []
T1_DROPS_RNGS = [[1,2], [4,5], [2,3], [1,2], [3,6], [1,10]]
T1_DROPS = [[1,0], [3,0], [10,0], [2,10], [1.5,0], [2,0]]
#for t in T1_DROPS:
#        print("")
#        print("COVERED: %s" % str(T1))
#        print("MERGING: %s" % str(t))
#        T1 = mergeRng(T1, t)
#        print("RESULTS: %s" % str(T1))

print(whenLineCovered([1,3], T1_DROPS))
