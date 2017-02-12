def first_half(str):
  str = str[:len(str)/2]
  return str

str = raw_input("Enter a string: ")

print(first_half(str))