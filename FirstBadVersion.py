# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    
# should be in O(log n) because binary search

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        mid = None
        
        while left <= right:
            print ('left: ' + str(left) )
            print('right: ' + str(right))
            mid = (right - left)//2 + left
            print('mid: ' + str(mid))
            if isBadVersion(mid) is True:
                # below was added other wise if n=3 and firstbadversion = 2 it will fail
                # this checks of at end of search when l,r, and m are close 
                if isBadVersion(mid-1) is False:
                    return mid
                right = mid - 1
            else:
                left = mid + 1
            
        return mid
        