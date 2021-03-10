import datetime

class CustomError (Exception):

    def __init__(self, nomber_false):
        self.nomber_false = nomber_false

    def __str__(self):
        return repr(self.nomber_false)

def  day_of_the_week():
    try:
        dict_week = {1:"monday",2:"tuesday",3:"wednesday",4:"thursday",5:"friday",6:"saturday",7:"sunday"}
        day = int(input("Enter please number day of the week : "))
        if (day < 0 or day > 8 ):
            raise CustomError("Day of the week is incorect")
        else:
            day_week = dict_week[day]
            print(day_week)

    except CustomError as e:
        print("We obtain error : ",e.nomber_false)
    except ValueError as e:
        print(e)

day_of_the_week()
