import time

import Adafruit_MCP3008

#CLK = 18
#MISO = 9
#MOSI = 10
#CS = 25
CLK = 18
MISO = 17
MOSI = 27
CS = 22


mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

while True:



    v = (mcp.read_adc(0) / 1023.0) * 3.3


    if v   > 2.8 :
      dist = -1
    elif v  > 2.0 :
      dist = 10
    elif v >  1.6:
      dist = 15
    elif v > 1.4:
      dist = 20
    elif v > 1.1:
      dist = 25
    elif v > 0.9:
      dist = 30
    elif v > 0.7:
      dist = 40
    elif v > 0.6:
      dist = 50
    elif v > 0.5:
      dist = 60
    elif v > 0.4:
      dist = 70
    elif v > 0.3:
      dist = 80
    else:
      dist = 9999

    #dist2 = (6787 /(v-3))-4


    dist2 = 16.2537 * v ** 4 - 129.893 * v ** 3 + 382.268 * v ** 2 - 512.611 * v + 301.439


    print("volts" +str(v)+ "  mapping calc " +str(dist) + " original math " + str(dist2) )


   # print("cm  " + str(dist) + " calc " + str(dist2) + " volts " + str(v ) +"   6050 method " +str(6050/v) )
   # print("\n\nDistanz: %.2f cm   " % dist )
    #print("Distanz: %.2f cm   " % dist2 )
    #print("Distanz: %2.5f  " % v )
    time.sleep(.5)

