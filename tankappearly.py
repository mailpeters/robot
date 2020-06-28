import RPi.GPIO as GPIO
from tankmotionclass import TankMotion
import time


TheTank = TankMotion(24, 23, 25, 5, 6, 13)
TheTank.Initialize()


#servo setup

nServoPinOut = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(nServoPinOut, GPIO.OUT)
p = GPIO.PWM(nServoPinOut, 50)
p.start(7.5)



while (1):

    #servo scan left to right, 5 positions 180 degrees facing front

    # move servo

    # measure distance
    # get heading


    p.ChangeDutyCycle(2.5)  # turn towards 0 degree
    print("0")
    time.sleep(1)  # sleep 1 second

    p.ChangeDutyCycle(5)  # turn towards 0 degree
    print("45")
    time.sleep(1)  # sleep 1 second

    p.ChangeDutyCycle(7.5)  # turn towards 90 degree
    print("90")
    time.sleep(1) # sleep 1 second

    p.ChangeDutyCycle(10)  # turn towards 90 degree
    print("135")
    time.sleep(1)  # sleep 1 second

    p.ChangeDutyCycle(12.5)  # turn towards 180 degree
    print("180")
    time.sleep(1)  # sleep 1 second


    x = input()

    if x == 'g':
        print("go")

        TheTank.Go()


    elif x == 's':
        print("stop")
        TheTank.Stop()


    elif x == 'f':
        print("forward")
        TheTank.Forward()

    elif x == 'b':
        print("backward")

        TheTank.Backward()



    elif x == 'l':
        print("low")

        TheTank.Speed("L")


    elif x == 'm':
        print("medium")
        TheTank.Speed("M")



    elif x == 'h':
        print("high")
        TheTank.Speed("H")

    elif x == 'e':
        print("exit")
        TheTank.Cleanup()
        break

    elif x == 'r':
        print("spin right")
        TheTank.Spin("R")

    elif x == 'q':
        print("spin left")
        TheTank.Spin("L")




    else:
        print("<<<  wrong data  >>>")
        print("please Oneenter the defined data to continue.....")