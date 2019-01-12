from gpiozero import PWMOutputDevice
from time import sleep
 
#///////////////// Define Motor Driver GPIO Pins /////////////////
# Motor A, Left Side GPIO CONSTANTS
PWM_FORWARD_LEFT_PIN = 26   # IN1 - Forward Drive
PWM_REVERSE_LEFT_PIN = 19   # IN2 - Reverse Drive
# Motor B, Right Side GPIO CONSTANTS
PWM_FORWARD_RIGHT_PIN = 13  # IN1 - Forward Drive
PWM_REVERSE_RIGHT_PIN = 6   # IN2 - Reverse Drive
 
# Initialise objects for H-Bridge PWM pins
# Set initial duty cycle to 0 and frequency to 1000
forwardLeft = PWMOutputDevice(PWM_FORWARD_LEFT_PIN, True, 0, 1000)
reverseLeft = PWMOutputDevice(PWM_REVERSE_LEFT_PIN, True, 0, 1000)
 
forwardRight = PWMOutputDevice(PWM_FORWARD_RIGHT_PIN, True, 0, 1000)
reverseRight = PWMOutputDevice(PWM_REVERSE_RIGHT_PIN, True, 0, 1000)
 
 
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
 
def reverseDrive():
    forwardLeft.value = 0
    reverseLeft.value = 1.0
    forwardRight.value = 0
    reverseRight.value = 1.0

def forwardTurnLeft():
    forwardLeft.value = 0.2
    reverseLeft.value = 0
    forwardRight.value = 0.8
    reverseRight.value = 0
 
def forwardTurnRight():
    forwardLeft.value = 0.8
    reverseLeft.value = 0
    forwardRight.value = 0.2
    reverseRight.value = 0
 
 
def main():
    allStop()
    print("forward")
    forwardDrive()
    sleep(5)
    reverseDrive()
    print("reverse")
    sleep(5)
    forwardTurnLeft()
    print("turn left")
    sleep(5)
    forwardTurnRight()
    print("turn right")
    sleep(5)
    allStop()
 
 
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
