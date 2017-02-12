def extra_end(str):
  str = str[len(str)-2:]
  return (str * 3)

str = raw_input("Enter a string: ")

print(extra_end(str))