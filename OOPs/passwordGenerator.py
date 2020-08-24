import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
digitNumber1=chr(random.randint(48,57))
digitNumber2=chr(random.randint(45,57))
pun1= chr(random.randint(33,38  ))
pun2= chr(random.randint(33,38))
#Generate more characters here
#....

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 +digitNumber1+digitNumber2 +lowercaseLetter1+lowercaseLetter2+ pun1 + pun2# + ....
password = shuffle(password)

#Ouput
print(password)