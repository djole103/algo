#not allowed ot use hashmap
def uniqChars(string):
        s = sorted(string)
        for i in range(1, len(s)):
                if s[i] == s[i-1]:
                        return False
        return True

assert uniqChars( "djtfhnf" ) == False
assert uniqChars("") == True
assert uniqChars("abc") == True
        
