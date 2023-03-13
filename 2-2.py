import RPi.GPIO as GPIO
import time

def bin_8 (a):
    b = bin(a)[2:]
    c = ('0'*(8-len(b)))+b
    d = list(c)
    e = [int(elem) for elem in d]
    return e


GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 1, 1, 1, 1, 1, 1, 1]
test = [2, 255, 127, 64, 32, 5, 0]

GPIO.setup(dac, GPIO.OUT)

for i in range(len(test)):
    GPIO.output(dac, bin_8(test[i]))
    time.sleep(1)
    GPIO.output(dac, 0)
    time.sleep(1)

GPIO.cleanup()
