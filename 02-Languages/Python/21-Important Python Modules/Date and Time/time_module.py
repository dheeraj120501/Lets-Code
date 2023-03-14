# Time module handles time-related tasks.
# time.time()   // It returns us the seconds of time that have elapsed since the Unix epoch. In simple words, it tells us the time in seconds that have passed since 1 January 1970.
# time.asctime()    // to print the local time onto the screen.
# time.sleep()  //  it sends the program to sleep for some defined number of seconds. It is like delayed the argument take delay time in sec.
# time.localtime()  // is used to convert the number of seconds to local time. argument is optional is not passed it will take time.time() as argument.

import time
initial = time.time()

k = 0
while(k<45):
    print("This is harry bhai")
    time.sleep(2)
    k+=1
print("While loop ran in", time.time() - initial, "Seconds")

initial2 =time.time()
for i in range(45):
    print("This is harry bhai")
print("For loop ran in", time.time() - initial2, "Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)