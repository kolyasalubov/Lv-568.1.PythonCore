fibonacci_numbers_first, fibonacci_numbers_second = 0, 1
fibonacci_numbers_end = int(input("Enter Fibonacci element number: : "))


if fibonacci_numbers_end == 1 : 
    print(fibonacci_numbers_first)
elif fibonacci_numbers_end == 2:
    print(fibonacci_numbers_first, fibonacci_numbers_second,)
else:
    print(fibonacci_numbers_first, fibonacci_numbers_second, end = ' ')
    while fibonacci_numbers_second < fibonacci_numbers_end :

        fibonacci_numbers_first , fibonacci_numbers_second = fibonacci_numbers_second, fibonacci_numbers_first  + fibonacci_numbers_second
        print(fibonacci_numbers_second, end = ' ') 
