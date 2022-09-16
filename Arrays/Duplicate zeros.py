class Solution:

    def duplicateZeros(self, arr):

        """
        Do not return anything, modify arr in-place instead.
        """
        zero_list = []

        for i, value in enumerate(arr):
            if value == 0:
                zero_list.append(i)
        zero_list_v2 = [i+j for i, j in enumerate(zero_list) if i+j<len(arr)]

        for j in zero_list_v2:

            #print(j)
            print(arr)
            for k in range(len(arr[j+1:])-1):
                #print(arr[j:][k+1], arr[j:][k])
                arr[j:][k+1] = arr[j:][k]

            print(arr)
            arr[j+1] = 0

        return arr




X = Solution()
array1 = [0, 10, -5, 0, -12, 13]
answer = X.duplicateZeros(array1)
print(answer)