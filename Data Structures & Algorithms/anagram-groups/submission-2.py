import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #count = [0] * 26
        ctr = 0
        res = {}
        
        for s in strs:
            count = [0] * 26
        
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            alphaTuple = tuple(count)
        
            if alphaTuple not in res:
                res[alphaTuple] = []
        
            res[alphaTuple].append(s)
        

       
        return list(res.values())
            