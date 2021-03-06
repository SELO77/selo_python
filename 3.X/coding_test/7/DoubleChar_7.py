# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
# double_char("String") ==> "SSttrriinngg"
#
# double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"
#
# double_char("1234!_ ") ==> "11223344!!__  "

def double_char(str):
  return ''.join("%s,"%(v * 2) for v in str)

result = double_char("abcd")
print(result)

# print("test".join(str(c) + "_" for c in range(5)))

# print("c".join(str(c) for c in range(3)))
print(c * 2 for c in ["h","e","l","l","o"])
