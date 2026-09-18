# First and Last Occurrence

N, X = map(int, input().split())

arr = list(map(int, input().split()))

first = -1
last = -1

for i in range(N):
    if arr[i] == X:
  
        if first == -1:
            first = i

        last = i

print(first, last)

# Time complexity: O(n)
# Space complexity: O(1)