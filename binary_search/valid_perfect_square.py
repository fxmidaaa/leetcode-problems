class Solution(object):
    def isPerfectSquare(self, num):
        lo = 1
        hi = num

        while lo <= hi:
            mid = (lo + hi) // 2
            square = mid * mid

            if square == num:
                return True

            if square < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False