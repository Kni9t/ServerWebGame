def CreateJSend(status, data = None, msg = None):

    if status != "error":
        response = {
        "status" : status,
        "data" : data
        }
    else:
        response = {
        "status" : status,
        "message" : msg
        }

    return response