
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ix_dict = {}
        
        for ix, el in enumerate(nums):
            if target - el in ix_dict:
                return [ix_dict[target - el], ix]
            
            ix_dict[el] = ix
        
        return []
