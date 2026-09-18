arr = list(map(int, input().split()))
n = int(input())

n = n % len(arr)

arr = arr[-n:] + arr[:-n]

print(*arr) 