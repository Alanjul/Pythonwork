import time
from private import privateClass
from timeWithProperties import Time
wake_up = Time(hour=6,minute=30)
print(wake_up)
print(wake_up.hour)
print(wake_up.time)
t = Time()
Time(hour=0, minute=0, second=0)
t.time = (12, 45,30)
print(t.time)
my_object = privateClass()
my_object.public_data
my_object.__private_data

