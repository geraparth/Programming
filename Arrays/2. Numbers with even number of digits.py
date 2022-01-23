class Solution:

    def findNumbers(self, nums) -> int:

        even_sum = 0

        for value in nums:
            quotient = value
            digits = 0

            while quotient > 0:
                quotient = quotient//10
                digits += 1

            if digits % 2 == 0:
                even_sum += 1

        return even_sum

x = Solution()
y = x.findNumbers([2345, 567, 6774, 56777])
print(y)






