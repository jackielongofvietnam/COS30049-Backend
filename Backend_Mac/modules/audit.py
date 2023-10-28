from utilities.response import response
from data_access.contracts import store_smart_contract_file

def audit_smart_contract(db, file_name, file_content):
    #Audit logic goes here
    store_file = store_smart_contract_file(file_name, file_content)

    result = "Suppose this is the result of audit" + file_name + file_content + str(store_file)

    return response(201, "Success", result)