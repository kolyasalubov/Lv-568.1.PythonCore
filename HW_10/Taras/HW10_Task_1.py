class CustomError(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


def user_age():
    try:
        enter_age = int(input('Enter your age: '))
        if enter_age < 0:
            raise CustomError('Your age cannot be negative')
        if enter_age > 120:
            raise CustomError('Unfortunately, but people do not live that long')
    except CustomError as e:
        print(e)
    else:
        if enter_age % 2 == 0:
            print('Your age is even')
        else:
            print('Your age is obb')

user_age()
