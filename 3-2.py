import sys
import RPi.GPIO as GPIO
from time import sleep

def ten_to_bin8(v):
    return [int(elem) for elem in bin(v)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

try:
    while (True):
        T = input();
        if T == 'q':
            sys.exit()
        elif not(T.isdigit()):
            print('Ввел буквы, попробуй еще раз')
        t = int(T)/256
        for i in range (256):
            GPIO.output(dac, ten_to_bin8(i))
            sleep(t)
        for i in range (255, -1, -1):
            GPIO.output(dac, ten_to_bin8(i))
            sleep(t)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()    

