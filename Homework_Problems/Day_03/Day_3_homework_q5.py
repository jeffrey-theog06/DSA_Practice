# Print All Pairs

N = int(input("Enter the number of elements: "))

A = list(map(int, input("Enter the elements: ").split()))

for i in range(N):
    for j in range(i + 1, N):
        print(f"({A[i]},{A[j]})")

# Time complexity: O(n^2)
# Space complexity: O(1)