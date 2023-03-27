import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

pwm = GPIO.PWM(7,1000)
pwm.start(0)

try:
    while(True):
        D = input()
        if D == 'q':
            sys.exit()
        elif not D.isdigit():
            print('Ввел буквы, попробуй еще раз')
        else: 
            pwm.ChangeDutyCycle(int(D))
            print("{:.2f}".format(int(D)*3.3/100))

finally:
    GPIO.output(7, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()    
