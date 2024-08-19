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
    index = time.find(":")
    if(index != -1):
        hour, minute = time.split(":")
        time = float(hour)+ round((float(minute)/60),2)
        return round(float(time),2)
    return float(time)
main()