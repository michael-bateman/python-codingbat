def without_end(str):
  str = str[1:len(str)-1]
  return str

str = raw_input("Enter a string: ")

print(without_end(str))