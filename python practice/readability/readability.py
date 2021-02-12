from cs50 import get_string
import math

text = get_string("Text:\n")

letters = 0
sentence = 0 
words = 1

# for loop to count letters, words and sentences as a array

for i in range(len(text)):
    if (text[i].isalpha()):
        letters += 1
    elif text[i] == " ":
        words += 1
    elif text[i] == "?" or text[i] == "!" or text[i] == ".":
        sentence += 1

L = (100 * letters / words)
S = (100 * sentence / words)

grade = round((0.0588 * L) - (0.296 * S) - 15.8)

if grade >= 1 and grade < 16:
    print("Grade", grade)
elif grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")

