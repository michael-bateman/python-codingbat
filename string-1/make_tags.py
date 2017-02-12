def make_tags(tag, word):
  tagopen = "<" + tag + ">"
  tagclose = "</" + tag + ">"
  return tagopen + word + tagclose

tag = raw_input("Enter a tag (ex. p): ")
word = raw_input("Enter a string: ")

print(make_tags(tag,word))