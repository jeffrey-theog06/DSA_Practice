def greatest_elements(arr):
    first = arr[0]
    second = arr[1]

    first_index = 1
    second_index = 2

    if second > first:
        first, second = second, first
        first_index, second_index = second_index, first_index

    for i in range(2, len(arr)):
        if arr[i] > first:
            second = first
            second_index = first_index

            first = arr[i]
            first_index = i + 1

        elif arr[i] > second:
            second = arr[i]
            second_index = i + 1

    print("First greatest = ", first, ", index = ", first_index)
    print("Second greatest = ", second, ", index = ", second_index)


arr = [10, 29, 9, 47, 26]

greatest_elements(arr)