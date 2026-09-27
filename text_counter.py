user = input("Enter text:").lower()

vowels = ["a","e","i","o","u"]

space = " "
s_pace = user.count(space)
print(f"Space in text: {s_pace}")

for vowel in vowels:
    value = user.count(vowel)
    print(f"{vowel} : {value}")

words = user.split()
word = len(words)
print(f"Words Count: {word}")

text = len(user)
print(f"text length: {text}")