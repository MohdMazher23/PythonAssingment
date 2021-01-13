class tv:
    def __init__(self,brand,model,screensize,resolution,price):
        self.brand=brand
        self.model=model
        self.screensize=screensize
        self.resolution=resolution
        self.price=price
    def features(self,display,controll):
        self.display=display
        self.controll=controll
        print("Display={} \n Controll={}".format(self.display,self.controll))

class smarttv(tv):
    def __init__(self,brand,model,screensize,resolution,price):
        super().__init__(brand,model,screensize,resolution,price)
    def smartfeature(self,wifi,screen_mirroring,bluethooth):
        self.wifi=wifi
        self.screen_mirroring=screen_mirroring
        self.bluethooth=bluethooth
        print("Wifi={}\n screenmirrring={} \n bluethooth={}".format(self.wifi,self.screen_mirroring,self.bluethooth))

    def info(self):
        print("******Properties*******")
        print("Brand={}\n Model={}\n ScreenSize={}\n Resolutiopn={}\n Price={}\n".format(self.brand,self.model,self.screensize,self.resolution,self.price))
        print("*******Features******")
        
        s1.features("Color","remote")
        print("*******Smart Features********")
        s1.smartfeature("Wifi Enabel","SUpport screen mirroring","4.0")

s1=smarttv("Samsung",2021,43,"1080p",38000)
s1.info()


#OUTPUT
"""
******Properties*******
Brand=Samsung
 Model=2021
 ScreenSize=43
 Resolutiopn=1080p
 Price=38000

*******Features******
Display=Color
 Controll=remote
*******Smart Features********
Wifi=Wifi Enabel
 screenmirrring=SUpport screen mirroring
 bluethooth=4.0

"""
