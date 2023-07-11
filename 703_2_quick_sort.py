def quick_sort(l):
    if len(l)<2:
        return(l)
    left = []
    right = []
    for i in l[1:]:
        if i < l[0]:
            left.append(i)
        else:
            right.append(i)
#    print(left,right)
    return(quick_sort(left)+[l[0]]+quick_sort(right))
A = [-10,1,3,1,4,10,3,9,4,5,1]
print(quick_sort(A))