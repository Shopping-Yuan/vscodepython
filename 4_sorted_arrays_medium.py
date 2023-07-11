#Strategy : maximize the lower bond of information at each step
class Solution:
#    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findMedianSortedArrays(self, nums1, nums2):
        def divide_array(a,left,right):
            if left+right == 0:
                i = len(a)*0.5
            else :
                i = len(a)*left/(left+right)
                print(len(a),left/(left+right))
            index = int(i)
            if i - index == 0:
                test_num = (a[index] + a[index-1])/2
                left_array = a[:index+1]
                right_array = a[index-1:]
            else :
                test_num = a[index]
                left_array = a[:index+1]
                right_array = a[index:]
            if len(left_array)<2:
                left_array = a[:2]
            if len(right_array)<2:
                right_array = a[-2:]
            print([test_num,left_array,right_array])
            return([test_num,left_array,right_array])
        
        n1_rest = nums1
        n2_rest = nums2
        left_cut = 0
        right_cut = 0
        half_len = 0.5*(len(nums1)+len(nums2))
        step = 0
        if  len(nums1)*len(nums2)>0:
            while True:
                pre_rest = (n1_rest,n2_rest)
                n1_test , n1_left , n1_right = divide_array(n1_rest,half_len-left_cut,half_len-right_cut)
                n2_test , n2_left , n2_right = divide_array(n2_rest,half_len-left_cut,half_len-right_cut)
                if n1_test >= n2_test : 
                    left_cut+= len(n2_rest)-len(n2_right)
                    right_cut += len(n1_rest)-len(n1_left)
                    n1_rest = n1_left
                    n2_rest = n2_right
                else :
                    right_cut += len(n2_rest)-len(n2_left)
                    left_cut+= len(n1_rest)-len(n1_right)
                    n1_rest = n1_right
                    n2_rest = n2_left
                step +=1
    #            print(n1_rest,n2_rest,left_cut,right_cut)
                if (n1_rest,n2_rest) == pre_rest:
                    break
            print(n1_rest,n2_rest)
        elif len(nums1) == 0:
            return(divide_array(nums2,0,0)[0])
        else:
            return(divide_array(nums1,0,0)[0])
        def sort_rest(n1,n2):
            x = []
            k = 0
            for i in range(len(n1)):
                for j in range(k,len(n2)):
                    if n1[i]<n2[j]:
                        break
                    else :
                        x.append(n2[j])
                        k = j+1
                x.append(n1[i])
            x += n2[k:]
            return(x)
        order = sort_rest(n1_rest,n2_rest)
        index = int((len(order)+(right_cut-left_cut))*0.5)
#        print(right_cut,left_cut,index)
        if (len(nums1)+len(nums2))%2 ==1:
            return(order[index])
        else:
            return((order[index]+order[index-1])/2)

n1 = []
#[1,2,6,7,8,9] 
n2 = [1]
#[3,4,5]
ans = Solution()
print(ans.findMedianSortedArrays(n1,n2))
