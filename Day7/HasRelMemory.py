class memory:
    def __init__(self,internal,secondary,ram):
        self.internal=internal
        self.secondary=secondary
        self.ram=ram

    def memoryinfo(self):
        print("Internal:{}\n Secondary:{}\n Ram:{}\n".format(self.internal,self.secondary,self.ram))

class mobileclass:
    def __init__(self,mobile,brand,price,memory):
        self.mobile=mobile
        self.brand=brand
        self.price=price
        self.memory=memory
    
    def mobileinfo(self):
        print("Mobile:{}\n Brand:{}\n Price:{}\n Memory Info".format(self.mobile,self.brand,self.price))
        self.memory.memoryinfo()

    
m1=memory("64 GB","16 GB","4 GB")
m2=mobileclass("Samart Phone","Samsung",20000,m1)
m2.mobileinfo()

#OUTPUT
"""
python HasRelMemory.py
Mobile:Samart Phone
 Brand:Samsung
 Price:20000
 Memory Info
Internal:64 GB
 Secondary:16 GB
 Ram:4 GB


"""