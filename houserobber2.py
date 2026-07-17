class solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(houses):
            prev1, prev2 = 0, 0
            for amount in houses:
                temp = prev1
                prev1 = max(prev2 + amount, prev1)
                prev2 = temp
            return prev1
        
        # Rob houses from index 0 to n-2 and from index 1 to n-1
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
    #runtime=0ms memory=12.30mb