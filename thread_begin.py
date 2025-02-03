#speeding up program with threading to help share data
import threading

def funct1():
    for x in range(5):
        print ( x)
funct1()
def function2():
    for y in range(10):
        print(y)
#funct1()
#function2()
t1 = threading.Thread(target=funct1)
t2 = threading.Thread(target=function2)
t1.start() #threads can only be used once, need to redefine if you want to reuse
t1.join() #pauses the main programm
print ("thread rules")
t2.start()

#pause the main program
