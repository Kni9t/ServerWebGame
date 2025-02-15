def CreateJSend(status, name, data, err = None):

    if status != "error":
        response = {
        "status" : status,
        "data": {
            name: data
            }
        }
    else:
        response = {
        "status" : status,
        "message" : err,
        "data": {
            name: data
            }
        }

    return response