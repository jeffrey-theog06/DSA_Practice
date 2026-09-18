n = int(input("Enter no of attendance set: "))

# for i in range(n):
#     attendance = input("Enter the attendance in 0(absent) and 1(present): ").split()
#     absent = attendance.count('0')

#     if absent == 0:
#         print("No absentees")
#     else:
#         print(f"{absent} students are absent")


# Without built in functions 
for i in range(n):
    attendance = input("Enter the attendance in 0(absent) and 1(present) with space: ")

    absent = 0

    for j in attendance:
        if j == '0':
            absent += 1

    if absent == 0:
        print("No absentees")
    else:
        print(f"{absent} students are absent")

# Printing with percentage of attendance