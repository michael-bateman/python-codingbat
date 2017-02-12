def sum_double(a, b):
  if(a == b):
    return ((a + b) * 2)
  else:
    return (a + b)

a = input("Enter a number: ")
b = input("Enter a second number: ")

print(sum_double(a,b))