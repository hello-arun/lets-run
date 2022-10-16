# Solution as submitted by me on https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ss = strs.copy()
        dicts={}
        for i,s in enumerate(strs):
            ss[i] = ''.join(sorted(s))
        for i,s in enumerate(ss):
            if s in dicts:
                dicts[s].append(strs[i])
            else:
                dicts[s]=[strs[i]]
        output=[]
        for key in dicts:
            output.append(dicts[key])
        return output
    
