import random

def infiniteMonkeys():

    text = "WhenshallwethreemeetagainInthunderlightningorinrain"

    for i in text:
        if random.randint(65, 122) != ord(i):
            return False
        
    return True
