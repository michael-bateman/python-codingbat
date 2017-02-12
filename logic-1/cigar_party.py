def cigar_party(cigars, is_weekend):
  if(is_weekend == "yes"):
    return (cigars >= 40)
  else:
    return (40 <= cigars <=60)

cigars = input("How many cigars?: ")
is_weekend = raw_input("Is it a weekend? (yes or no) ")

print(cigar_party(cigars,is_weekend))