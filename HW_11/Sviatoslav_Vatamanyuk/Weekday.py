weekday = (1, 2, 3, 4, 5, 6, 7)
weeknum = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
numday = list(zip(weekday, weeknum))
try:
    x = int(input("Please enter num of weekday "))
    if x <= 0:
        raise IndexError("You cannot enter number below 1 ")
    elif x > 7:
        raise IndexError("You cannot enter number above 7 ")
    else:
        print(numday[x-1])
except IndexError as e:
    print(e)
