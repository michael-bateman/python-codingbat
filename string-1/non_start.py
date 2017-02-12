def non_start(a, b):
  a = a[1:]
  b = b[1:]
  return a + b

a = raw_input("Enter a string: ")
b = raw_input("Enter a second string: ")

print(non_start(a,b))