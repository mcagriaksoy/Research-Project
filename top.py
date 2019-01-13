
import RPi.GPIO as GPIO
import time
from gpiozero import PWMOutputDevice
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)
trig = 38
echo = 18
p.start(7.5)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

# Motor A, Left Side GPIO CONSTANTS

PWM_FORWARD_LEFT_PIN = 26  # IN1 - Forward Drive
PWM_REVERSE_LEFT_PIN = 19  # IN2 - Reverse Drive

# Motor B, Right Side GPIO CONSTANTS

PWM_FORWARD_RIGHT_PIN = 13  # IN1 - Forward Drive
PWM_REVERSE_RIGHT_PIN = 6  # IN2 - Reverse Drive

forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)

forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)

count = 0
count_right = 0
count_left = 0
# count int is defined for sampled values of maze. @alp @salim
# I assumed we'll solve maze in 20 steps so, while condition loops runs 20 step only!

maze = [8][11]
maze[8][11] = 1
maze[0][0] = 0


def allStop():
    forwardLeft.value = 0
    reverseLeft.value = 0
    forwardRight.value = 0
    reverseRight.value = 0


def forwardDrive():
    forwardLeft.value = 1.0
    reverseLeft.value = 0
    forwardRight.value = 1.0
    reverseRight.value = 0
    count += 1


def reverseDrive():
    forwardLeft.value = 0
    reverseLeft.value = 1.0
    forwardRight.value = 0
    reverseRight.value = 1.0
    count -= 1


def forwardTurnLeft():
    forwardLeft.value = 0.2
    reverseLeft.value = 0
    forwardRight.value = 0.8
    reverseRight.value = 0
    count_left += 1


def forwardTurnRight():
    forwardLeft.value = 0.8
    reverseLeft.value = 0
    forwardRight.value = 0.2
    reverseRight.value = 0
    count_right += 1


def main():
    try:
        GPIO.output(trig, False)
        time.sleep(0.2)
        while maze[8][11] != 0:

            p.ChangeDutyCycle(2.7)
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

            if distance > 10:
                forwardDrive()
                maze[0][count] = 0
            else:
                p.ChangeDutyCycle(7.5)
                GPIO.output(trig, True)
                time.sleep(0.00001)
                GPIO.output(trig, False)

                while GPIO.input(echo) == 0:
                    start1 = time.time()

                while GPIO.input(echo) == 1:
                    stop1 = time.time()

                time2 = stop1 - start1
                distance2 = (time2 * 34300) / 2

                if distance2 > 10:
                    forwardTurnRight()
                    maze[count_right][count] = 0

                    p.ChangeDutyCycle(2.7)
                    GPIO.output(trig, True)
                    time.sleep(0.00001)
                    GPIO.output(trig, False)

                    while GPIO.input(echo) == 0:
                        start1 = time.time()

                    while GPIO.input(echo) == 1:
                        stop1 = time.time()

                    time2 = stop1 - start1

                    distance_9 = (time2 * 34300) / 2

                    if distance_9 > 10:
                        forwardDrive()
                    else:
                        p.ChangeDutyCycle(7.5)
                        GPIO.output(trig, True)
                        time.sleep(0.00001)
                        GPIO.output(trig, False)

                        while GPIO.input(echo) == 0:
                            start1 = time.time()

                        while GPIO.input(echo) == 1:
                            stop1 = time.time()

                        time2 = stop1 - start1
                        distancexx = (time2 * 34300) / 2
                        if distancexx > 10:
                            forwardTurnRight()
                        else:
                            forwardTurnLeft()
                else:
                    p.ChangeDutyCycle(13.8)
                    GPIO.output(trig, True)
                    time.sleep(0.00001)
                    GPIO.output(trig, False)

                    while GPIO.input(echo) == 0:
                        start1 = time.time()

                    while GPIO.input(echo) == 1:
                        stop1 = time.time()

                    time2 = stop1 - start1
                    distance000 = (time2 * 34300) / 2

                    if distance000 < 10:
                        reverseDrive()
                        maze[count_left][count] = 0

                    else:
                        forwardTurnLeft()
                        maze[count_left][count] = 0

                        p.ChangeDutyCycle(2.7)
                        GPIO.output(trig, True)
                        time.sleep(0.00001)
                        GPIO.output(trig, False)

                        while GPIO.input(echo) == 0:
                            start1 = time.time()

                        while GPIO.input(echo) == 1:
                            stop1 = time.time()

                        time2 = stop1 - start1
                        distance3 = (time2 * 34300) / 2

                        if distance3 < 10:
                            p.ChangeDutyCycle(7.5)
                            GPIO.output(trig, True)
                            time.sleep(0.00001)
                            GPIO.output(trig, False)

                            while GPIO.input(echo) == 0:
                                start1 = time.time()

                            while GPIO.input(echo) == 1:
                                stop1 = time.time()

                            time2 = stop1 - start1
                            distance4 = (time2 * 34300) / 2
                            if distance4 < 0:
                                forwardTurnLeft()
                            else:
                                forwardTurnRight()
                        else:
                            forwardDrive()

							

if __name__ == "__main__":
    """ This is executed when run from the command line """
main()
