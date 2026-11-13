from threading import Semaphore, Thread

A: int = 0
B: int = 0
C: int = 3

# SUMA = 56

sem2 = Semaphore(0)
sem3 = Semaphore(0)
sem4 = Semaphore(0)

def threadP1():

    global A
    global B
    global C
    A = 10
    B = B + 5
    C = C + A
    print("Thread P1 is done...")
    sem2.release()

def threadP2():

    global A
    global B
    global C

    sem2.acquire()
    B = B + C
    sem3.release()
    sem2.acquire()
    A = A + B
    print("Thread P2 is done...")

def threadP3():

    global A
    global B
    global C

    sem3.acquire()
    C = B + 10
    sem4.release()
    sem3.acquire()
    A = 2 * A
    B = B + A
    print("Thread P3 is done...")

def threadP4():
    sem4.acquire()
    global A
    global B
    global C
    print("Sum result: ",A," + ",B," + ",C," = ",(A + B + C))
    print("Thread P4 is done...")
    sem2.release()
    sem3.release()

threads = []

threads.append(Thread(target=threadP4))
threads.append(Thread(target=threadP3))

threads.append(Thread(target=threadP1))
threads.append(Thread(target=threadP2))



for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("All done")
