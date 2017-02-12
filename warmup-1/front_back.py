def front_back(str):
  first = str[0]
  last = str[len(str)-1]
  mid = str[1:len(str)-1]
  return last + mid + first

str = raw_input("Enter a string: ")

print(front_back(str))