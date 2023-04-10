import RPi.GPIO as GPIO
from time import sleep

def ten_to_bin8(v):
    return [int(elem) for elem in bin(v)[2:].zfill(8)]

def adc():
    w = 0
    for i in range (7, -1, -1):
        w += 2**i
        GPIO.output(dac, ten_to_bin8(w))
        sleep(0.001)
        if GPIO.input(comp) == 0:
            w -= 2**i
    return(w)

def volume(a, n):
    x = round(a/n*8)
    ans = [0 for i in range(8)]
    for i in range(x):
        ans[i] = 1
    return ans[::-1]


GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)
comp = 4
GPIO.setup(comp, GPIO.IN)
troyka = 17
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)


try:
    while True:
        i = adc()
        print(i,"{:.2f}v".format(3.3*i/256))
        if i != 0:
            GPIO.output(leds, volume(i, 63))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
