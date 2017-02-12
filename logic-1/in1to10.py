def in1to10(n, outside_mode):
  if(outside_mode == "yes"):
    if(n <= 1 or n >= 10):
      return True
    else:
      return False
      
  elif(1 <= n <= 10):
    return True
  else:
    return False

n = input("Enter a number: ")
outside_mode = raw_input("Outside mode? (yes or no) ")

print(in1to10(n,outside_mode))