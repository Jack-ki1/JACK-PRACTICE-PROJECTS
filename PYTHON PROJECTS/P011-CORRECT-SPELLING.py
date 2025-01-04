import spellchecker

corrector = spellchecker

word = input("Enter a word: ")

if word in corrector:
    print("correct")
else:
    correct_word = corrector.correction(word)
    print(f"correct word is {correct_word}")
    