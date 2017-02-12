def combo_string(a, b):
  a_length = len(a)
  b_length = len(b)
  if(a_length > b_length):
    return b + a + b
  else:
    return a + b + a

a = raw_input("Enter a string: ")
b = raw_input("Enter a second string: ")

print(combo_string(a,b))