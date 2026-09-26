class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()
        #L,R = "",""
        #isP = True
        #r = -1
        L = 0
        R = len(string) - 1

        while L < R:
        #for l in range(len(string) // 2):
            #L = string[l]
            #R = string[r]
            if not string[L].isalnum():
                L += 1
                l = string[L]
                r = string[R]
            elif not string[R].isalnum():
                R -= 1
                l = string[L]
                r = string[R]
            #    r -=1
            #    R = string[r]
            elif string[L] != string[R]:
                return False
            #    print(r)
            #    r -=1
            #    continue
            else:
                L += 1
                R -= 1
                l = string[L]
                r = string[R]
        return True
    





