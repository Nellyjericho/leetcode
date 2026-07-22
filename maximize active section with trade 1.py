# class Solution(object):
#     def maxActiveSectionsAfterTrade(self, s):

#         # Add boundary 1s
#         t = "1" + s + "1"

#         # Build blocks
#         blocks = []
#         count = 1

#         for i in range(1, len(t)):
#             if t[i] == t[i-1]:
#                 count += 1
#             else:
#                 blocks.append((t[i-1], count))
#                 count = 1

#         blocks.append((t[-1], count))

#         # Find maximum gain
#         best_gain = 0

#         for i in range(1, len(blocks)-1):
#             # Current block is 1s and is surrounded by 0s
#             if blocks[i][0] == '1':
#                 if blocks[i-1][0] == '0' and blocks[i+1][0] == '0':

#                     # The removed 1s disappear,
#                     # the surrounding 0s become 1s
#                     gain = blocks[i-1][1] + blocks[i+1][1]

#                     best_gain = max(best_gain, gain)

#         return s.count('1') + best_gain

#runtime = 1958ms memory = 25.64mb

#this was definetly not the most efficient solution but it worked and was easy to understand. I will try to make it more efficient in the next version.

class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        
        # Track the length of the previous contiguous group of zeroes
        # Initialize to float('-inf') to handle strings with no left zero neighbor correctly
        pre_zero_len = float('-inf')
        max_gain = 0
        
        i = 0
        while i < n:
            j = i + 1
            while j < n and s[j] == s[i]:
                j += 1
                
            curr_len = j - i
            
            if s[i] == '1':
                # Base case: Any naturally occurring '1's always contribute to our initial active sections
                ans += curr_len
            else:
                # If we encounter a zero block, it can potentially merge with a previous zero block
                # that was separated by a '1' block. The gain would be pre_zero_len + curr_zero_len.
                max_gain = max(max_gain, pre_zero_len + curr_len)
                pre_zero_len = curr_len
                
            i = j
            
        # Add the maximum extra gain achieved via an optimal trade operation
        return ans + max_gain
    #this is the most efficient according to the runtime