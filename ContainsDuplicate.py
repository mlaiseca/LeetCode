class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # O(n) space
        # retreival is O(1)
        d = {}
        
        # O(n) time
        if nums:
            for i in nums:
                if i in d:
                    return True
                else:
                    d[i] = True
        return False
        