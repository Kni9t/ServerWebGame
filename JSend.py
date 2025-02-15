def CreateJSend(status, name, data):
    response = {
        "status" : status,
        "data": {
            name: data
            }
        }

    return response