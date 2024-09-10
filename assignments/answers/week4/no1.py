class Clock:
    def __init__(self, hour, minutes, seconds):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
    
    def get_time(self):
        if self.seconds >= 60:
            minutes = self.seconds // 60 
            self.minutes += minutes
            self.seconds = self.seconds % 60

        if self.minutes >= 60:
            hours = self.minutes // 60 
            self.hour += hours
            self.minutes = self.minutes % 60
        
        print(f"{self.hour} hrs {self.minutes} mins {self.seconds} sec")                       
    
    def tick(self):
        self.seconds += 1
    
    def display(self):
        hour_display = self.hour
        time_period = "AM"
        if self.hour >= 12:
            time_period = "PM"
            if self.hour > 12:
                hour_display = self.hour - 12
        elif self.hour == 0:
            hour_display = 12
        print(f"{hour_display:02}:{self.minutes:02}:{self.seconds:02} {time_period}")
                

time = Clock(2,59,1200)
time.get_time()
time.tick()
time.display()
