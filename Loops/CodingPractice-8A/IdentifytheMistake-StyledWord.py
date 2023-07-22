word = input()
first_char = word[0]
new_word = first_char
for each_char in range(1 , len(word)):
    new_word = new_word + "-" + word[each_char]
print(new_word)