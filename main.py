import threading
import time
import os
import json

from flask import Flask, request, Blueprint, jsonify, make_response
from resource import data, importantData, handleApi

app = Flask(__name__)


def threadFn(value: str):
    global data
    for i in range(5):
        print("Thread {} --> Value: {} | Data: {}".format(i, value, data["api_cache"]))

    return "Thread Complete"


@app.route("/test", methods=["POST"])
def mainFn():
    global data
    global value
    requestData = request.get_json()
    worker_pid = os.getpid()

    # th = threading.Thread(target=handleApi, args=(requestData["api"],))
    # th.start()
    # th.join()
    with data["api_cache"].get_lock():
        handleApi(requestData["api"])
    
    for i in range(1):
        apis = ','.join([str(x) for x in data["api_cache"]])
        print("Main {} --> PID: {} | Data: {}".format(i, worker_pid, apis,))
        # value = value+1

    
    return jsonify({"status": "Success"})


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port="8055", debug=True,
#             threaded=True)
