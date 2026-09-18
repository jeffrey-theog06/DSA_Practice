class Solution:
    def rearrange(self, arr):
        arr.sort()

        left = 0
        right = len(arr) - 1
        temp = []

        while left <= right:
            temp.append(arr[right])
            right -= 1

            if left <= right:
                temp.append(arr[left])
                left += 1

        arr[:] = temp