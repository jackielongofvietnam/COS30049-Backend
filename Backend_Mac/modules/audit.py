from utilities.response import response
from data_access.contracts import insert_audit_report

def audit_smart_contract(db, file_name, file_content):
    #Audit logic goes here

    #Push audit result to db and store smart contract file
    status = "risky"
    vulnerabilities = [
        [
            {
                "issue": "Smart contract is risky",
                "suggestion": "Fix it"
            },
            {
                "issue": "Smart contract is dangerous",
                "suggestion": "Remove it"
            }
        ]
    ]
    audit_report = insert_audit_report(db, file_name, file_content, status, vulnerabilities)

    result = "Suppose this is the result of audit" + file_name + file_content + str(audit_report)

    return response(201, "Success", result)