import random
word_length = int(input("Enter the length of password: "))
characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = "".join(random.sample(characters, word_length))
print(password)