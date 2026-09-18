arr = list(map(int, input().split()))
n = int(input())

n = n % len(arr)

# Reverse entire array
arr.reverse()

# Reverse first part
arr[:len(arr)-n] = reversed(arr[:len(arr)-n])

# Reverse second part
arr[len(arr)-n:] = reversed(arr[len(arr)-n:])

print(*arr)