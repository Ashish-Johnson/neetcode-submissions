class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
       
        # Build hashmap
        for i, n in enumerate(nums):
            idx[n] = i

        # Search
        for i, n in enumerate(nums):
            diff = target - n
            if diff in idx and idx[diff] != i:
                return [i, idx[diff]]

        return []