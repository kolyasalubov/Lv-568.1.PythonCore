# Changing int to float elements in list

# One solution

int_list= [2, 3, 4, 5]
float_list = []
for x in int_list:
    float_list.append(float(x))
print(float_list)
print(type(float_list[1]))

# Other solution

#l1 = [1,2,3,4,5]
#l2 = [float(i) for i in l1]
#print (l2)

# Notes

#x=[2,4,6]
#print(type(x))
#print(type(x[1]))
#a=float(x[1])
#print(type(a))