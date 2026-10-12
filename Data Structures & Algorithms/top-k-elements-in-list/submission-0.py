class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s={}
        for i in nums:
            s[i]=s.get(i,0)+1
        so=sorted(s,key=s.get,reverse=True)
        return so[:k]


        