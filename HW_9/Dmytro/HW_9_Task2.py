def week(date):
    try:
        DAYS = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
        print(DAYS[date-1])
    except IndexError as e:
        print(e)


week(date=int(input("Day of week ")))
