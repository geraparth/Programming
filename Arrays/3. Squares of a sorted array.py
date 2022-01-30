class Solution:

    def merge_sort(self, arr):
        """

            To sort an array in ascending order using merge sort. Time complexity : O(nlogn)

            Parameters :  array

            Returns : Sorts the array
        """

        if len(arr) > 1:

            #Recursively dividing the left and right arrays
            mid = len(arr)//2
            l = arr[:mid]
            r = arr[mid:]
            self.merge_sort(l)
            self.merge_sort(r)

            i = j = k = 0

            #Merging elements in ascending order
            while i < len(l) and j < len(r):

                if l[i] < r[j]:
                    arr[k] = l[i]
                    i += 1

                else:
                    arr[k] = r[j]
                    j += 1
                k += 1

            #Checking if there are any elements remaining
            while i < len(l):
                arr[k] = l[i]
                i += 1
                k += 1

            while j < len(r):
                arr[k] = r[j]
                j += 1
                k += 1

    def sortedSquares(self, nums):
        """

            To square and sort elements of an array in ascending order.

            Parameters :  nums  - Array with numerical elements

            Returns : Squares and Sorts the array
                """

        #Using merge sort to square and sort
        nums = [value**2 for value in nums]
        self.merge_sort(nums)
        return nums


X = Solution()
array1 = [1, 10, -5, -7, -12, 13]
answer = X.sortedSquares(array1)
print(answer)