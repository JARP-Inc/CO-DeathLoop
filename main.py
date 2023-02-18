import bogoSort
import timeCheck
import weather
import timeit

 

def main():

    start = timeit.default_timer()

    timesRan = 0
    exit = 0
    while(exit < 1):
        timesRan += 1
        
        #3, 2, 4, 1, 0, 5, 7, 2, 6, 7, 8, 3
        if bogoSort.bogoSort([3, 2, 4, 1, 0, 5]) == True:
            exit += 1
        
        if timeCheck() == True:
            exit += 1

        if weather() == True:
            exit += 1

        if timesRan%3.142 == 0:
            exit += 1

    stop = timeit.default_timer()

    print('Time: ', stop - start)
    


main()


#List of the 9 unlikely things:
#1: perfect bogo sort                               Done
#2: current time is at 0 seconds                    Done
#3: stellaris dashboard (use if all else fails)
#4: weather api                                     Done
#5: check computer's ram usage
#6: is times ran divisible by pi                    Done