import random

#this is done

def bogoSort(arrayIn):
    shuffle(arrayIn)
    return is_sorted(arrayIn)

def shuffle(arrayIn):
    
    for i in range(0, len(arrayIn)):
        r = random.randint(0, len(arrayIn)-1)
        arrayIn[i], arrayIn[r] = arrayIn[r], arrayIn[i]


def is_sorted(arrayIn):
    
    for i in range(0, len(arrayIn)-1):

        if (arrayIn[i] > arrayIn[i+1]):
            return False

    return True

