s_string(string):
    # TODO: Implement me
    if string == None: return None
    if len(string) <=2:
        return string
    compressed = ""
    counter = 1
    for i in range(1, len(string)):
        print("INDEX: %d\nCOUNTER: %d\nCOMPRESSED: %s" %(i, counter, compressed))
        if string[i] != string[i-1]:
            if counter <= 2:
                compressed += counter * string[i-1]
            else:
                compressed += string[i-1] + str(counter)
            counter = 1
        else:
            counter +=1
    if counter > 2:
        compressed += string[-1] + str(counter)
    else:
        compressed += counter * string[-1]
    return compressed
compress_string("AAABCCDDDD")
