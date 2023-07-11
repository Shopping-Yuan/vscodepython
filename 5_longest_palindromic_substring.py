"""
class Solution:
    def longestPalindrome(self, s) :
        longest = s[0]
        now = s[0]
        state = 0
        index_1 = -1
#        index_2 = -1
        if len(s)<2:
            return(s)
        for x in s[1:]:
            index = len(now)-1
            while(state == 0)&(index >= 0):  
                if x!= now[index]:
                    index -=1
                else:
                    if index == len(now)-1:
#                        now = now[-1]
                        index_1 = len(now)-2
                        state = 2
                    elif index == len(now)-2:
                        state =1
                        index_1 = len(now)-2
#                        index_2 = len(now)-1
                    else :
#                        now = now[index+1:]+x
                        break
            print(now,index_1,state)
            if state == 1:
                if index_1 >=0:
                    if now[index_1] == x:
                        index_1 -= 1
                    else :
                        if len(longest)< len(now[index_1+1:-1]):
                            longest = now[index_1+1:-1]
#                            now = now[index_2:]
                        state =0
                else :
                    if len(longest)< len(now):
                        longest = now
#                    now = now[index_2:]
                    state =0
            print(now,index_1,state,longest)
            if state ==2:
                if x != now[-1]:
                    if len(longest)< len(now[index_1+1:-1]):
                        longest = now[index_1+1:-1]
#                    now = now[-1]
                    state = 1
            now += x                    
        if (state == 1) & (len(longest)< len(now[index_1+1:])):
            longest = now[index_1+1:]
            print(now,index_1,state,longest)
        if (state ==2) & (len(longest)< len(now[index_1:])):
            longest = now[index_1:]
        return(longest)
"""

class Solution:
    def longestPalindrome(self, s) :
        if len(s)<2:
            return(s)
        elif len(s) == 2:
            if s[0] == s[1]:
                return(s)
            else:
        longest = s[0]
        now = s[0]
        left_edge_id = 0
        center_value_id = 1
        right_edge_id =1
        for id_x , x in enumerate(s[2:]):
            now = s[left_edge_id:right_edge_id+1]
            if center_value_id == id_x -1 & (x == s[center_value_id]):
                center_value_id += 1
                right_edge_id += 1
                now += x
            else:
                    if x == s[left_edge_id]:
                        left_edge_id -=1
                        right_edge_id += 1
                        now += x
                    else:
                        if longest <= now:
                            longest = now
                        left_edge_id = id_x -1
                        right_edge_id += 1
            if left_edge_id < 0:
                if longest <= now:
                    longest = now
                left_edge_id = center_value_id -1
        





S = "xaabacxcabaaxcabaax"
S2 = "babad"
sol = Solution()
print(sol.longestPalindrome(S))



                   
         