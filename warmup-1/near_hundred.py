def near_hundred(n):
  return ((90 <= n <= 110) or (190 <= n <= 210))

n = input("Enter a number: ")

print(near_hundred(n))