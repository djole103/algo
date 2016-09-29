N, K = map(int, raw_input().split(' '))
ints = map(int, raw_input().split(' '))

result = 0

for i in range(len(ints)):
        for j in range(i,len(ints)):
                if abs(ints[i] - ints[j]) == K:
                        result += 1
print(result)
