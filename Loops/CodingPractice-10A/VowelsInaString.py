word = input()
resultant_of_vowels = ""
for each_char in word:
    for each_char_in_vowels in "aeiou":
        if each_char == each_char_in_vowels:
            resultant_of_vowels = resultant_of_vowels + each_char
print(resultant_of_vowels)
