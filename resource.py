from multiprocessing import Lock
from multiprocessing.sharedctypes import Array, Value
from ctypes import c_char_p
import time

global data
global value
lock = Lock()

# data = Manager().dict()
data = {}
data["api_cache"] = Array(c_char_p, [b""]*10)
value = Value('d', 0.0)

importantData = {
    "status": None
}

def handleApi(api):
    global data
    api = api.encode("ascii")
    print("API: ", api)
    if api in data["api_cache"]:
        for i in range(len(data["api_cache"])):
            print(data["api_cache"][i], end=", ")
        
        print("\nAPI found")
        temp = api
        for i in range(len(data["api_cache"])):
            if(data["api_cache"][i]!=api):
                temp2 = data["api_cache"][i].decode("ascii")
                data["api_cache"][i] = temp
                temp = temp2.encode("ascii")
            elif(data["api_cache"][i] == api):
                data["api_cache"][i] = temp
                break

        importantData["status"] = True
        # return True
    else:
        print("API not found")
        for i in range(len(data["api_cache"])):
            print(data["api_cache"][i], end=", ")
        time.sleep(2)
        temp = api
        if(data["api_cache"][0] == None):
            data["api_cache"][0] = api
        else:
            for i in range(len(data["api_cache"])):
                if(data["api_cache"][i] != None):
                    temp2 = data["api_cache"][i].decode("ascii")
                    data["api_cache"][i] = temp
                    temp = temp2.encode("ascii")
                else:
                    data["api_cache"][i] = temp
                    break;
        
        importantData["status"] = True
        # return true