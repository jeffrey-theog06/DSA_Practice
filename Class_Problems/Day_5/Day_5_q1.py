# After reading each element, print the max value seen so far. 

def maxSoFar():
    userInp = list(map(int, input().split()))
    max = 0
    for i in userInp:
        if i > max:
            max = i
        print(max)

maxSoFar()