class Solution:
    def deleteElement(self, arr, ele):
        for i in range(len(arr)):
            if arr[i] == ele:
                arr.pop(i)
                break