def ispalin(s):
    s = s.lower()
    return s == s[::-1]
print(ispalin("madam"))
print(ispalin("false"))