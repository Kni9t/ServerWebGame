def CreateJSend(status, data, err = None):

    if status != "error":
        response = {
        "status" : status,
        "data" : data
        }
    else:
        response = {
        "status" : status,
        "message" : err
        }

    return response