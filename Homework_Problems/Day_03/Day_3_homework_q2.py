# Placement Cutoff Count

N, C = map(int, input("Enter two integers for N and C: ").split())

scores = list(map(int, input("Enter integers representing candidates scores: ").split()))

count = 0

for score in scores:
    if score >= C:
        count += 1

print(count)

# Time complexity: O(n)
# Space complexity: O(1)