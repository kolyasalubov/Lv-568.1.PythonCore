## numbers that are divisible by... in range

y=int(input("Enter a maximum range number: "))

div_2=[]
div_3=[]
indiv=[]

for x in range (1,y+1):
    if x%2==0:
        div_2.append(x)
    elif x%3==0:
        div_3.append(x)
    elif x%3!=0 and x%2!=0:
        indiv.append(x)
print("Divisible by 2 numbers: ", div_2)
print("Divisible by 3 numbers: ", div_3)
print("Indivisible by 2 and 3 numbers: ", indiv)
print("Finish")