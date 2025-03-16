def CreateJSend(status, name, data = None, err = None):

    if status != "error":
        response = {
        "status" : status
        }
    else:
        response = {
        "status" : status,
        "message" : err
        }
        
    if (data is not None):
        response["data"] = {
            name: data
        }

    return response