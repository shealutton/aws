import threading
import time

def sleeper (n, name):
    print('Hi, I am thread {}. Sleeping for 5 seconds.'.format(name))
    time.sleep(3)
    print('{} is now awake'.format(name))


t1 = threading.Thread(target = sleeper, args = (5, 'Jane'))
t2 = threading.Thread(target = sleeper, args = (5, 'Mary'))
t1.start()
t2.start()
print('Hello parent thread')
