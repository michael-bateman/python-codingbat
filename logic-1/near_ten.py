def near_ten(num):
  return num % 10 in [0,1,2,8,9,10]

num = input("Enter a number: ")

print(near_ten(num))