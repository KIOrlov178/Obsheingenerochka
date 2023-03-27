import sys
import RPi.GPIO as GPIO

def ten_to_bin8(v):
    return [int(elem) for elem in bin(v)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

try:
    while(True):
        a = input('input 0-255  ')
        if a == 'q':
            sys.exit()

        elif (',' in a) or ('.' in a):
            print('Ввел дробное, попробуй еще раз')
        elif '-' in a:
            print('Ввел отрицательное, попробуй еще раз')
        elif not(a.isdigit()):
            print('Ввел буквы, попробуй еще раз')
        elif int(a) > 255:
            print('Ввел больше 255, попробуй еще раз')
        
        else:
            GPIO.output(dac, ten_to_bin8(int(a)))
            print("{:.4f}".format((int(a)/256)*3.3))
       
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

