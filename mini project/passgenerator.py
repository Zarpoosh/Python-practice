# password generator 
import string, random
strings=string.ascii_letters
pasword="".join(random.sample(strings , 10))
print(pasword)