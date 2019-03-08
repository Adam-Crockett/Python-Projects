word = input("Enter a word or sentence to see if it is a palindrome: ")

print(True if word == word[::-1] else False)
