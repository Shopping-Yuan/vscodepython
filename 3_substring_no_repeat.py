class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        not_repeat = ""
        not_repeat_l = 0
        not_repeat_lmax = 0
        for i in s:
            for j in not_repeat:
                if j == i:
                    if j==not_repeat[-1]:
                        not_repeat = ""
                        not_repeat_l = 0
                    else :
                        j_index = not_repeat.index(j)
                        not_repeat = not_repeat[j_index+1:]
                        not_repeat_l -= j_index+1
            not_repeat += i
            not_repeat_l += 1
            if not_repeat_lmax < not_repeat_l:
                not_repeat_lmax = not_repeat_l
        return(not_repeat_lmax)