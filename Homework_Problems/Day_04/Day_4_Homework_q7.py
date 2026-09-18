class Solution:
    def modifyArray(self, arr):
        n = len(arr)
        result = [-1] * n

        for x in arr:
            if x != -1:
                result[x] = x

        arr[:] = result