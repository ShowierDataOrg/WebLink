from .MikeDev_code.cloudlink import CloudLink

class client:
    def __init__(self,debug=False,ip="127.0.0.1"):
        self.__backend__ = CloudLink(debug)
        self.debug = debug
        self.ip = ip
    
    def run(self):
        self.__backend__.client(self.ip)

    def SendPacket(self,msg):
        self.__backend__.sendPacket(msg)
    def stop(self):
        self.__backend__.stop(False)

    def Callback(self,function,id=None):
        self.__backend__.callback(id if not None else function.name,function)
        