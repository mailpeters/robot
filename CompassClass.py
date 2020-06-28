import FaBo9Axis_MPU9250
import time
import sys

mpu9250 = FaBo9Axis_MPU9250.MPU9250()

try:
    while True:
#        accel = mpu9250.readAccel()
#        print(" ax = ", (accel['x']))
#       print(" ay = ", (accel['y']))
#       print(" az = ", (accel['z']))

#       gyro = mpu9250.readGyro()
#       print(" gx = ", (gyro['x']))
#       print(" gy = ", (gyro['y']))
#       print(" gz = ", (gyro['z']))

        mag = mpu9250.readMagnet()
        print("z mx = ", (mag['x']))
        print("z my = ", (mag['y']))
        print("z mz = ", (mag['z']))


        time.sleep(2)

except KeyboardInterrupt:
    sys.exit()