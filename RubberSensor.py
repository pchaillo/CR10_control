import serial


class RubberSerialDuino:

    def __init__(self):
        # PARAM7TRES
        self.port = '/dev/ttyACM0'
        self.baud = 115200

        #INIT
        self.res = 0
        self.ser = serial.Serial(self.port,self.baud) 

    def UpdateSensors(self):

        ligne_raw = str(self.ser.readline())
        #print("ligneraw:"+str(ligne_raw))

        ligne_cut = ligne_raw.split("'")
        ligne_cut2 = ligne_cut[1].split("\\")
        ligne_cut3 = ligne_cut2[0].split(";")
        #print("ligneraw:"+str(ligne_raw))
        #print("lignecut:"+str(ligne_cut))
        print("lignecut3:"+str(ligne_cut3[1]))


        try:
            self.res = float(ligne_cut3[1])

        except:
            print('Attention, lecture impossible')
            a = 0

    def GetRes(self):
        # print(str(self._pres)) # for debug
      return self.res
