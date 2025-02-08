def notset(lst):
    uniq_lst = []
    for elem in lst:
        if elem not in uniq_lst:
            uniq_lst.append(elem)
    return uniq_lst
print(notset([1,2,1,31,4,14,5,25,5,5,31,4]))
