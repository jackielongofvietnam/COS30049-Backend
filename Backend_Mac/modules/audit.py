from utilities.response import response

def audit_smart_contract(file_name, file_content):
    #Audit logic goes here

    result = "Suppose this is the result of audit" + file_name + file_content

    return response(201, "Success", result)