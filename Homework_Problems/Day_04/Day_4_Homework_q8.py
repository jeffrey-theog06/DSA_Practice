class Solution:
    def arrange(self, arr):
        n = len(arr)

        for i in range(n):
            old = arr[i] % n
            new = arr[old] % n
            arr[i] += new * n

        for i in range(n):
            arr[i] //= n