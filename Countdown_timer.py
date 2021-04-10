import time
class timer(object):
    def count_timer(t):
        while t>0:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")             # Here \r to delete the previous print and then print new value of iteration
            time.sleep(1)
            t -= 1
            
        print("Timer completed..!!!")

T = timer
T.count_timer(int(input("Please enter time in seconds: ")))
