# Print Fibonacci numbers up to the entered number n, using cycles

x=int(input("Please enter the maximum allowed sequence value, x, (x>=2) : "))
fibonacciSeries=[0,1]
for y in range(2,x):
	#next element in series = sum of its previous two numbers
	nextElement = fibonacciSeries[y-1] + fibonacciSeries[y-2]
	#check if nextElement is less or than inputted "x"
	if nextElement <= x:
		#append the element to the series
	    fibonacciSeries.append(nextElement)
	else:
		break
print(fibonacciSeries)
