#Fibonacci Series
value = input("Enter a value: ")

try:
    n = int(value)

    if value.strip().lstrip("-").isdigit():
        a, b = 0, 1

        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b
    else:
        print("Only int data type is accepted.")

except ValueError:
    print("Only int data type is accepted.")
