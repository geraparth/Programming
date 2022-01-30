class Solution:

    def merge_sort(self, arr):

        if len(arr) > 1:
            mid = len(arr)//2
            l = arr[:mid]
            r = arr[mid:]
            self.merge_sort(l)
            self.merge_sort(r)

            i = j = k = 0

            while i < len(l) and j < len(r):


                if l[i] < r[j]:
                    arr[k] = l[i]
                    i += 1

                else:
                    arr[k] = r[j]
                    j += 1
                k += 1

            while i < len(l):
                arr[k] = l[i]
                i += 1
                k += 1

            while j < len(r):
                arr[k] = r[j]
                j += 1
                k += 1

    def sortedSquares(self, nums):

        nums = [value**2 for value in nums]
        self.merge_sort(nums)
        return nums


X = Solution()
array1 = [1, 10, -5, -7, -12, 13]
answer = X.sortedSquares(array1)
print(answer)