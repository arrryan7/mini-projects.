import random
import string

characters = string.ascii_letters + string.punctuation + string.digits

passwordLen = 10
password = ""

#list comprehension
#password = "".join([random.choice(characters) for i in range(passwordLen)])

for i in range(passwordLen):
    password += random.choice(characters)

print("your random password:",password)