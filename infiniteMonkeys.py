import random

def infiniteMonkeys():

    text = "When shall we three meet again. In thunder, lightning, or in rain?"

    for i in text:
        if random.randint(65, 122) != ord(i):
            return False
        
    return True
