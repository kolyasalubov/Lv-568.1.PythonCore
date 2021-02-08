numeric = input("four-digit number: ")
print(sum(map(int, list(numeric)))) 
print(numeric[ : : -1])
print(sorted(list(numeric)))