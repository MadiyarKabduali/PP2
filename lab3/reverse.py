def rs(sent):
    return " ".join(sent.split()[::-1])
print(rs("we are ready"))
