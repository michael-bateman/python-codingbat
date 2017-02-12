def sorta_sum(a, b):
  sum = a + b
  if(10 <= sum <= 19):
    return 20
  else:
    return sum

a = input("Enter a number: ")
b = input("Enter a second number: ")

print(sorta_sum(a,b))