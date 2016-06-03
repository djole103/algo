def compress(s):
        if len(s) < 2: return s
        counter = 1
        curr = s[0]
        result = ""
        for i in range(1,len(s)):
                if s[i] == curr:
                        counter += 1
                else:
                        if counter > 1:
                                result = result + curr + str(counter)
                                counter = 1
                        else:
                                result += curr
                        curr = s[i]
        return result

print(compress("aaabbcde"))
