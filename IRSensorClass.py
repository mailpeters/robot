import Adafruit_MCP3008

class IRSensor:

    #constructor sets the pin values
    def __init__(self, nCLK, nMISO, nMOSI, nCS ):
        self.nCLK = nCLK
        self.nMISO = nMISO
        self.nMOSI = nMOSI
        self.nCS = nCS

    def Init(self):
        self.mcp = Adafruit_MCP3008.MCP3008(self.nCLK, self.nCS, self.nMISO, self.nMOSI)

    def GetDistance2(self):

        v = (self.mcp.read_adc(0) / 1023.0) * 3.3

        if v > 2.8:
            dist = -1
        elif v > 2.0:
            dist = 10
        elif v > 1.6:
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

        return dist


    def GetDistance(self):

        #v = (self.mcp.read_adc(0) / 1023.0) * 3.3
        v = self.mcp.read_adc(0)

        #  R = 6787/(Va2d−3)−4.

        dist = ( 6787/ (v-3) )-4

        return dist

