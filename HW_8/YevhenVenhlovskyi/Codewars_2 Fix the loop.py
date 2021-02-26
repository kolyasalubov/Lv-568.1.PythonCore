## Fix the loop!

def list_animals(animals):
    y=1
    str_1=""
    for x in animals:
        str_1 += (str(y) + ". " + x + "\n")
        y+=1
    print(str_1)

animals = [ 'dog', 'cat', 'elephant' ]
list_animals(animals)

# Answer ('1. dog\n2. cat\n3. elephant\n')
