def missing_char(str, n):
  front = str[:n]
  back = str[n+1:]
  return front + back

str = raw_input("Enter a string: ")
n = input("Enter the missing letter as a number: ")

print(missing_char(str,n))