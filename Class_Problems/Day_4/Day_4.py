def PrintASCIITable():
    for i in range(0, 255):
        if i <= 32 or i >= 127:
            print(f"ASCII number: {i} - Character: Null")
        else:
            print(f"ASCII number: {i} - Character: {chr(i)}")

PrintASCIITable() 