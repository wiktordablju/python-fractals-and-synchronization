from threading import Semaphore, Thread
import time

# A C B A C

semA = Semaphore(0)
semB = Semaphore(0)
semC = Semaphore(0)

def printA(ntimes):
    for i in range(ntimes):
        semA.acquire()
        print('A ', end="")        
        semB.release()
        time.sleep(1)

def printB(ntimes):
    for i in range(ntimes):
        semA.release()
        semB.acquire()
        semC.release()
        semB.acquire()
        print('B ', end="")
        semA.release()
        semB.acquire()
        semC.release()
        time.sleep(1)
        
def printC(ntimes):
    for i in range(ntimes):

        semC.acquire()
        print('C ', end="")
        semB.release()
        
        time.sleep(1)
       
how_many = 10
threads = []

threads.append(Thread(target=printB, args=(how_many,)))
threads.append(Thread(target=printA, args=(2*how_many,)))
threads.append(Thread(target=printC, args=(2*how_many,)))

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("\nAll done")
