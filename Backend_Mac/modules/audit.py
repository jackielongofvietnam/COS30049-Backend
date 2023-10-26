from utilities.response import response

def auditSmartContract(fileName, fileContent):
    #Audit logic goes here

    result = "Suppose this is the result of audit" + fileName + fileContent

    return response(201, "Success", result)