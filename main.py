import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

uppercaseLetter=chr(random.randint(65,90))
lowercaseLetter=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
lowercaseLetter3=chr(random.randint(97,122))
lowercaseLetter4=chr(random.randint(97,122))
lowercaseLetter5=chr(random.randint(97,122))
number=chr(random.randint(48,57))
number2=chr(random.randint(48,57))
symbol=chr(random.randint(33,64))

password = uppercaseLetter + lowercaseLetter + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + lowercaseLetter5 + number + number2 + symbol
password = shuffle(password)

print(password)