try:
    days_of_the_week = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    choose = int(input('enter number of the day: '))
    if choose == 1:
        print(days_of_the_week[choose], f'  --is the {choose}st day of the week')
    elif choose == 2:
        print(days_of_the_week[choose], f'  --is the {choose}nd day of the week')
    elif choose == 3:
        print(days_of_the_week[choose], f'  --is the {choose}rd day of the week')
    else: 
        print(days_of_the_week[choose], f'  --is the {choose}th day of the week')
except KeyError as e:
    print('There are only 7 days(1-7)')
except ValueError as e:
    print('You need to enter numbers(1-7)')