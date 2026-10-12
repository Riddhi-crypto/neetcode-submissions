class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1={}
        if len(s)!=len(t):
            return False
        for i in s:
            s1[i]=s1.get(i,0)+1
        for j in t:
            if j not in s1:
                return False
            s1[j]-=1
            if s1[j]<0:
                return False
        return True
        

        