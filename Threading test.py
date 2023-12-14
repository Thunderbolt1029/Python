import threading, time

def play1():
    time.sleep(1)
    print(1)
    
def play2():
    print(2)

    
threading.Thread(target=play1).start()
threading.Thread(target=play2).start()
