#Ask user for time in main
#Call convert function
#Compare time given to breakfast times
#If similar, print the corresponding eating time
#7:00-8:00 breakfast
#12:00-1300 lunch
#18:00-19:00 dinner

def main():
    time = convert(input("What is the current time? "))
    if time >= 7.0 and time <= 8.0:
        print ("It's breakfast")
    elif time >= 12.0 and time <= 13.0:
        print("It's lunch time")
    else:
        print("It's dinner!")

def convert(time):
    hour, minute =time.split(":")
    if("am" in time or "pm" in time):
        grab=time[-2:]
        hour = float(hour)
        minute = float(minute[:-2])
        return usePmAm(hour,grab,minute)
    time = float(hour)+ round((float(minute)/60),2)
    return round(float(time),2)

def isIt(hour, grab):
     if("am" in grab and hour == 12.0):
         return 24
     elif("pm" in grab and hour == 12.0):
         return 12
     return hour

def usePmAm(hour, grab, minute):
    if("pm" in grab and hour != 12):
        return isIt(hour)  + 12 + ((minute/60))
    print(isIt(hour,grab)+float(minute/60))
    return float(round(isIt(hour,grab)+((minute/60))))
main()