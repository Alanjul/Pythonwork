#class Time rea-write properties
class Time:
    """Class Time with read-write properties"""

    def __init__(self, hour=0, minute=0, second=0):
        #private variables
        self.hour = hour
        self.minute = minute
        self.second = second
    @property #declarate
    def hour(self):
        #return the hour
        return self._hour
    @hour.setter
    def hour(self, hour):
        #set hour
        if not(0 <= hour <= 23):
            raise ValueError(f"Invalid ({hour} hour")
        self._hour = hour
    @property
    def minute(self):
        #return minutes
        return self._minute
    @minute.setter
    def minute(self, minute):
        #set  minutes
        if not(0 <= minute <= 59):
            raise ValueError(f"Invalid ({minute}minute")
        self._minute = minute
    @property
    def second(self):
        #return the second
        return self._second
    @second.setter
    def second(self, second):
        #set seconds
        if not(0 <= second <= 59):
            raise ValueError(f"Invalid ({second}second")
        self._second = second

    #set time objects
    def set_time(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        #construct a constructor like object in string formation
    def __repr__(self):
        #Return Time string for repr()
        return(f"Time(hour ={self.hour}, minutes= {self.minute}"+
               f"seconds = {self.second})")
    def __str__(self):
        #returns Time string in 12 hour clock format
        return (('12' if self.hour in (0,12) else str(self.hour%12))+
                f':{self.minute:0>2}:{self.second:0>2}'+
                ('AM'if self.hour < 12.0 else 'PM'))
    @property
    def time(self):
        #return  hour, minutem and second as tuple
        return (self.hour, self.minute, self.second)
    @time.setter
    def time(self, time_tuple):
        #set time from tuple containing hour, minute and second
        self.set_time(time_tuple[0], time_tuple[1], time_tuple[2])

