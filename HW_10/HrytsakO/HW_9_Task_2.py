try:
    number = int(input("Enter a number: "))
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Satuday", "Sunday"]
    print(days[number % 7 - 1])
except ValueError:
    print("Error, invalid number")

