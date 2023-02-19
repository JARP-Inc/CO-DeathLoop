import time
import threading
import random


x = False

def racer(value):
    global x
    x = bool(value)


def horseRace():

    threads = []
    for i in range(10):
        if random.randint(0,100) == 1:
            threads.append(threading.Thread(target=racer, args=(random.randint(0,1),)))
        else:
            threads.append(threading.Thread(target=racer, args=(0,)))


    [n.start() for n in threads]
 
    [n.join() for n in threads]

    return x

