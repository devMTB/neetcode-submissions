from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = [0] * len(s)
        lt = [0] * len(t)
        ctr = 0
        for char in s:
            ls[ctr] = s[ctr]
            ctr += 1
        ctr = 0
        for char in t:
            lt[ctr] = t[ctr]
            ctr += 1
        print(ls)
        print(lt)

            

        cntS = Counter(ls)
        print(cntS)
        
        cntT = Counter(lt)
        print(cntT)

        if cntS == cntT:
            return True
        else:
            return False




