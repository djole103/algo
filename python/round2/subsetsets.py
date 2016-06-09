def subsets(ss, results = []):
        if ss and ss not in results:
                results.append(ss)
        for i in range(len(ss)):
                        results = subsets(ss[:i] + ss[i+1:], results)
        return results

TEST = [1,2,3, 4]
print(subsets(TEST))

