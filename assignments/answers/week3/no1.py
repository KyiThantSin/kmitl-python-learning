def convert_time(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    if hours >= 12:
       time = "PM"
       if hours > 12:
           hours = hours - 12  
    else: 
       time = "AM" 
       if hours == 0:
           hours = 12
    return hours,minutes,time
   
        
hours, minutes, time = convert_time("20:24")
print(hours,":",minutes,time)