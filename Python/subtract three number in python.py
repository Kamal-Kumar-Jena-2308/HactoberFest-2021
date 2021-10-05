#program for subtracting three numbers
while True:
    try:
        x=int(input("Enter the first number: "))
        y=int(input("Enter the second number: "))
        z=int(input("Enter the third number: "))
        t=x-y-z
        print(f"The difference of {x}, {y} nad {z} is",t)
        break
    except ValueError:
        print("Enter a valid number")
        continue
