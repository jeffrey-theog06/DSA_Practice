def avgEvenAndOdd(arr):
    even_sum = odd_sum = 0
    even_count = odd_count = 0

    for x in arr:
        if x % 2 == 0:
            even_sum += x
            even_count += 1
        else:
            odd_sum += x
            odd_count += 1

    even_avg = even_sum / even_count if even_count else 0
    odd_avg = odd_sum / odd_count if odd_count else 0

    return even_avg, odd_avg

t = int(input("Enter the number of test cases: "))

for case in range(1, t + 1):
    arr = list(map(int, input("Enter the elements of the array: ").split()))

    even_avg, odd_avg = avgEvenAndOdd(arr)

    print(f"For Test Case {case}")
    print(f"Even Average: {even_avg:.2f}")
    print(f"Odd Average: {odd_avg:.2f}")