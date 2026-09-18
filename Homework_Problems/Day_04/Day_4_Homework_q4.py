arr = list(map(int, input().split()))
index = list(map(int, input().split()))

result = [0] * len(arr)

for i in range(len(arr)):
    result[index[i]] = arr[i]

print(*result)