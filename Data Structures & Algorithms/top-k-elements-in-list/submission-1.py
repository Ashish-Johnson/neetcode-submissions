class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {} 
        l =[] 
        for i in nums: 
            if i in d.keys(): 
                d[i]+=1 
            else: 
                    d[i] = 1 
        sorted_d = sorted(d.items(), key = lambda x: x[1],reverse = True) 
        
        return [sorted_d[j][0] for j in range(k)]