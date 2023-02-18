from datetime import datetime


def timeCheck():

    
    time = datetime.now().strftime('%S')

    if time == 0:
        return True

    return False