import bogoSort
import timeCheck
import weather
import RAM
import infiniteMonkeys
import speedCheck
import stellarisDashboard
import horseRace
import timeit

 

def main():

    start = timeit.default_timer()

    timesRan = 0
    while(True):
        timesRan += 1

        if(timesRan%1000000 == 0):
            print(timesRan)
        
        #3, 2, 4, 1, 0, 5, 7, 2, 6, 7, 8, 3
        if bogoSort.bogoSort([3, 2, 4, 1, 0, 5]) != True:
            continue
        
        if timeCheck.timeCheck() != True:
            continue

        if weather.weather() != True:
            continue

        if timesRan%3.142 != 0:
            continue

        if RAM.RAM() != True:
            continue

        if infiniteMonkeys.infiniteMonkeys() != True:
            continue
        
        if speedCheck.speedCheck() != True:
            continue
        
        if stellarisDashboard.stellarisDashboard() != True:
            continue

        if horseRace.horseRace() != True:
            continue

        break
        

    stop = timeit.default_timer()

    print('Time: ', stop - start)
    print("Times ran: " + timesRan)
    


main()


#List of the 9 unlikely things:
#1: perfect bogo sort                               Done
#2: current time is at 0 seconds                    Done
#3: weather api                                     Done
#4: check computer's ram usage                      Done
#5: is times ran divisible by pi                    Done
#6: infinite monkeys principle                      Done
#7: speed check                                     Done
#8: stellaris dashboard (use if all else fails)     Done
#9: race conditions                                 Done?