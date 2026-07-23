class Solution(object):
    def firstBadVersion(self, n):
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
    #runtime = 15ms memory = 12.40mb