class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        existing_set = set()
        for num in nums:
            if num in existing_set:
                return True
            existing_set.add(num)

        return False