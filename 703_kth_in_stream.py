'''
class KthLargest:
    def __init__(self, k, nums):
        self.kth = k
        self.list = nums
        self
        for i in range(len(self.list)):
            j = i
            while j > 0:
                if self.list[j]>self.list[j-1]:
                    c = self.list[j]
                    self.list[j] = self.list[j-1]
                    self.list[j-1] = c
                    j-=1
                else : 
                    break
    def add(self, val):
        self.list.append(val)
        k = len(self.list)-1
        while k > 0:
            if self.list[k]>self.list[k-1]:
                c = self.list[k]
                self.list[k] = self.list[k-1]
                self.list[k-1] = c
                k-=1
            else:
                break
        return(self.list[self.kth-1])
'''
"""
class KthLargest:
    def __init__(self, k, nums):
        self.kth = k
        self.list = nums
        self.number_list = []
        for i in range(10):
            count = 0
            for j in self.list:
                if 9-i == j:
                    count +=1
            self.number_list.append(count)             
    def add(self, val):
        order_sum = 0
        kth_value = -1
        for k in range(10):
            if val == 9-k:
                self.number_list[k]+= 1
            order_sum += self.number_list[k]
            if (order_sum >= self.kth) & (kth_value < 0):
                kth_value = 9-k
        return(kth_value)
"""

class KthLargest:
#sort list 
    def __init__(self, k, nums):
        def merge_sort(l):
            if len(l)>=2:
                index = len(l)//2
                (i,j) = (0,0)
                result = []
                left = merge_sort(l[:index])
                right = merge_sort(l[index:])
                while((i < len(left))&(j < len(right))):
                    if left[i]>=right[j]:
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
    
        self.kth = k
        self.list = nums
        try:
            self.k_list = merge_sort(self.list[0:k])
        except:
            self.k_list = merge_sort(self.list)
        
        l_id = len(self.k_list)
        while l_id < len(self.list):
            self.k_list.append(self.list[l_id])
            index = len(self.k_list)-1
            while index > 0:
                if self.k_list[index]>self.k_list[index-1]:
                    c = self.k_list[index]
                    self.k_list[index] = self.k_list[index-1]
                    self.k_list[index-1] = c
                    index-=1
                else :
                    break
            del self.k_list[-1]
            l_id+=1

    def add(self, val):
        self.k_list.append(val)
        k = len(self.k_list)-1
        while k > 0:
            if self.k_list[k]>self.k_list[k-1]:
                c = self.k_list[k]
                self.k_list[k] = self.k_list[k-1]
                self.k_list[k-1] = c
                k-=1
            else:
                break
#        print(self.k_list,k)
        if len(self.k_list)>self.kth:
            self.k_list = self.k_list[:self.kth]
        return(self.k_list[-1])

A = [-10,1,3,1,4,10,3,9,4,5,1]
x = KthLargest(7,A)
print(x.add(3))