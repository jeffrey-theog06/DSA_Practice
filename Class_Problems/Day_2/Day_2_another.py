n = int(input())
ids = list(map(int, input().split()))

if len(set(ids)) == n:
    print("YES")
else:
    print("NO")