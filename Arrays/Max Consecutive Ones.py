class Solution:

    def findMaxConsecutiveOnes(self, nums) -> int:

        consecutive_ones = 0
        max_consecutive_ones = 0

        for key, value in enumerate(nums):

            if value == 1:
                consecutive_ones += 1

            elif value == 0:
                consecutive_ones = 0

            if consecutive_ones >= max_consecutive_ones:
                max_consecutive_ones = consecutive_ones

        return max_consecutive_ones
