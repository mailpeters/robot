import RPi.GPIO as GPIO
from tankmotionclass import TankMotion
import time

TheTank = TankMotion(24, 23, 25, 5, 6, 13)
TheTank.Initialize()

#servo setup
nCenterPosition = 7.5
nServoPinOut = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(nServoPinOut, GPIO.OUT)
p = GPIO.PWM(nServoPinOut, 50)
p.start(nCenterPosition)


#CLK = 18
#MISO = 17
#MOSI = 27
#CS = 22
from IRSensorClass import IRSensor
IRSensor = IRSensor(18,17,27,22)
IRSensor.Init()

nMinimumDrivingDistance = 9

# compass mpu
import FaBo9Axis_MPU9250
import time
mpu9250 = FaBo9Axis_MPU9250.MPU9250()


def largestIndex(arr):
    # Initialize maximum element
    MaxValue = 0
    MaxPosition = 0

    # Traverse array elements from second
    # and compare every element with
    # current max
    for x in range(0, len(arr)):
        current = int(arr[x])
        if arr[x] > MaxValue :
            MaxValue = arr[x]
            MaxPosition=x


    return MaxPosition


while (1):

    #servo scan left to right, 5 positions 180 degrees facing front

    # move servo

    # measure distance

    # note heading for each position

    Positions = [2.5,5,7.5,10,12.5]
    Distances = [0,0,0,0,0]
    Headings =  [-1,-1,-1,-1,-1]

    for x in range(0, len(Positions)):
        p.ChangeDutyCycle(Positions[x])  # turn towards 0 degree

        time.sleep(1)  # sleep 1 second

        Distances[x] = IRSensor.GetDistance()

        mag = mpu9250.readMagnet()

        Headings[x] = mag['y']

        #print(Distances[x])





    #pick the longest distance heading

    nLargestPosition = largestIndex(Distances)

    print(nLargestPosition)
    print(Distances)
    print(Headings)




    #turn vehicle to heading for the longest distance
    # turn slowly to the new heading  Headings[nLargestPosition)






    #begin moving again


    #set speed faster based upon distance, slower speed for shorter distances

    p.start(nCenterPosition)    # point directly frontwards



    # what if you are already too close?

    #move forward

    print("Driving Distance of " +str(Distances[nLargestPosition]) + " heading " + str(Headings[nLargestPosition]))



    TheTank.Spin("L")
    TheTank.Forward()
    #TheTank.Go()   #needed?


    #check distances constantly


    while True:
        time.sleep((0.5))
        x =IRSensor.GetDistance()
        if x < nMinimumDrivingDistance :
            print("too close" +str(x))
            break





    #too close, then stop

    TheTank.Stop()


    #loop back to the top and start over






