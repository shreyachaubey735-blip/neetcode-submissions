class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #using sets
        # use dict(), set() because both dictionary and set use {}.
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
        