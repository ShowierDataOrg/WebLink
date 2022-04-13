from .MikeDev_code.cloudlink import CloudLink
import traceback

class server:
    def __init__(self,ip="127.0.0.1", port=3000, threaded=False, throttle_usernames=False,debug=False):
        self.__backend__ = CloudLink(debug)
        self.debug = debug
        self.ip = ip
        self.port = port
        self.threaded = threaded
        self.throttle_usernames = throttle_usernames

    def run(self):
        """
        Blocking Call That Runs The Server 
        """
        try:
            self.__backend__.server(ip=self.ip,port=self.port,threaded=self.threaded,throttle_usernames=self.throttle_usernames)
        except Exception as exe:
            if self.debug:
                tracebac = traceback.format_exc()
                print(f"Error {str(exe)} error path: {tracebac}")

    def callback(self,func,callback_id):
        self.__backend__.callback(callback_id if not None else func.name,func)
    
    def setMOTD(self,MOTD,enable=True):
        self.__backend__.setMOTD(MOTD,enable)

    def SendPacket(self,msg):
        self.__backend__.sendPacket(msg)
    
    def GetBlockedIps(self):
        return self.__backend__.getIPBlocklist()
    
    def BlockIp(self,ip):
        self.__backend__.blockIP(ip)
    
    def KickClient(self,obj):
        self.__backend__.kickClient(obj)
    
    def Stop(self,abrupt=False):
        self.__backend__.stop(abrupt)
    
    def Trusted_accsess(self,enable,keys):
        self.__backend__.trustedAccess(enable,keys)
    
    def unblockIp(self,ip):
        self.__backend__.unblockIP(ip=ip)
