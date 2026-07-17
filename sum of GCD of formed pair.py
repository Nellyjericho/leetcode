class Solution(object):
    def gcdSum(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        prefixGCD = []
        mx = 0

        # Build prefixGCD
        for num in nums:
            mx = max(mx, num)
            prefixGCD.append(gcd(num, mx))

        # Sort
        prefixGCD.sort()

        # Pair smallest and largest
        answer = 0
        left = 0
        right = len(prefixGCD) - 1

        while left < right:
            answer += gcd(prefixGCD[left], prefixGCD[right])
            left += 1
            right -= 1

        return answer
    # runtime = 787ms memory = 22.52mb

