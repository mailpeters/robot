import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

CLK = 18
MISO = 17
MOSI = 27
CS = 22


# works see notes at bottom of demo web page

#CLK = 18
#MISO = 23
#MOSI = 24
#CS = 25


mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

while True:

    v = (mcp.read_adc(0) / 1023.0) * 3.3
    dist = 16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 301.439
    print(dist)
    time.sleep(0.5)