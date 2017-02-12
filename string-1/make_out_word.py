def make_out_word(out, word):
  outfirst = out[:2]
  outlast = out[2:]
  return outfirst + word + outlast

out = raw_input("Enter a string: ")
word = raw_input("Enter a second string: ")

print(make_out_word(out,word))