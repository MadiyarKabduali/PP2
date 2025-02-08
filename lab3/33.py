def has_33(nums):
    for i in range(0,len(nums)):
        if i == len(nums)-1:
            print(False)
            break
        else:
            if nums[i]==3 and nums[i+1]==3:
                print(True)
                break
    pass
has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])
