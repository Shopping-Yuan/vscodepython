def merge_sort(l):
    if len(l)>=2:
#        print(l)
        index = len(l)//2
        (i,j) = (0,0)
        result = []
        left = merge_sort(l[:index])
        right = merge_sort(l[index:])
        while((i < len(left))&(j < len(right))):
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else :
                result.append(right[j])
                j+=1
        if i < len(left):
            result += left[i:]
        else :
            result += right[j:]
        return(result)
    else : 
        return(l)
A = [-10,1,3,1,4,10,3,9,4,5,1]
print(merge_sort(A))