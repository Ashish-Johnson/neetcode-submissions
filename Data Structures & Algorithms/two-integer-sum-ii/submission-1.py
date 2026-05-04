class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res={}
        for i ,num in enumerate(numbers):
            diff = target - num
            if diff in res and res[diff] != i:
                return [res[diff]+1,i+1]
            res[num] = i