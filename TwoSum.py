class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        this_dict = {}
        pointer = 0
        
        for i in nums:
            #if i <= target:
            diff = target - i
            if diff in this_dict:
                return [this_dict[diff], pointer]
            if i not in this_dict:
                this_dict[i] = pointer
            pointer += 1
                    
                    
        