arr = list(map(int, input().split()))

i = 0

while i < len(arr) // 2:
    arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
    i += 1

print(*arr)