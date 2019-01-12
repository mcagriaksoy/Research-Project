import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)
trig = 38
echo = 18
p.start(7.5)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

try:
    GPIO.output(trig, False)
    
    time.sleep(2)
    while True:
        distance = 0
        p.ChangeDutyCycle(2.7)  # turn towards 90 degree
        print("0 derece")
        GPIO.output(trig, True)

        time.sleep(0.00001)

        GPIO.output(trig, False)


        while GPIO.input(echo) == 0:
            start1 = time.time()
            
        while GPIO.input(echo) == 1:
            stop1 = time.time()
           
        time2 = stop1 - start1
        distance = (time2 * 34300) / 2
        print(distance)
        time.sleep(2)
        p.ChangeDutyCycle(7.5)  # turn towards 0 degree
        print("90 derece")
        GPIO.output(trig, True)

        time.sleep(0.00001)

        GPIO.output(trig, False)


        while GPIO.input(echo) == 0:
            start1 = time.time()
            
        while GPIO.input(echo) == 1:
            stop1 = time.time()
           
        time2 = stop1 - start1
        distance = (time2 * 34300) / 2
        print(distance)
        time.sleep(2) # sleep 1 second
        p.ChangeDutyCycle(12.3) # turn towards 180 degree
        
        
        print("180 derece")
        GPIO.output(trig, True)

        time.sleep(0.00001)

        GPIO.output(trig, False)


        while GPIO.input(echo) == 0:
            start1 = time.time()
            
        while GPIO.input(echo) == 1:
            stop1 = time.time()
           
        time2 = stop1 - start1
        distance = (time2 * 34300) / 2
        print(distance)
        time.sleep(2) # sleep 1 second
        p.ChangeDutyCycle(7.5) # turn towards 180 degree
        
        
        print("90 derece")
        GPIO.output(trig, True)

        time.sleep(0.00001)

        GPIO.output(trig, False)


        while GPIO.input(echo) == 0:
            start1 = time.time()
            
        while GPIO.input(echo) == 1:
            stop1 = time.time()
           
        time2 = stop1 - start1
        distance = (time2 * 34300) / 2
        print(distance)
        time.sleep(2) # sleep 1 second
        
except KeyboardInterrupt:
    p.ChangeDutyCycle(2.5)
    GPIO.cleanup()
