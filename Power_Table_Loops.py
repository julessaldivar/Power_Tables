print("Learn your squares and cubes!\n")
while True:
    try:
        integer = int(input("Enter an integer: "))
        print("Number\t\tSquared\t\tCubed")
        print("=======\t\t=======\t\t=======")
        for i in range(1, integer + 1):
            squared = i ** 2
            cubed = i ** 3
            print(f"{i}\t\t{squared}\t\t{cubed}")
        decision = input("Continue? (y/n): ")
        if decision == 'n':
            break
    except ValueError:
        print("Please enter a valid integer.")

