from utilities.response import response
from data_access.contracts import insert_audit_report, store_file
import subprocess

def find_solution(sectionName):
    filePath = "../slither/Detector-Documentation.md"
    SectionFormat = sectionName.replace("-", " ")
    SectionLineInMarkDown = "## " + SectionFormat
    with open(filePath, 'r') as file:
        lines = file.readlines()
        foundOutSection = False
        foundOutRecommendation = False
        suggestions = ""
        
        for line in lines:
            # if we found out the section
            
            if line.lower().startswith(SectionLineInMarkDown):
                foundOutSection = True
                continue
            
            if foundOutSection and line.startswith("### Recommendation"):
                foundOutRecommendation = True
                continue
            
            if foundOutRecommendation and line.startswith("## "):
                return suggestions
            
            if foundOutRecommendation:
                suggestions += line
                suggestions += "\n"
                  
    return "Currently can not find out the suggestions yet"
                          

'''The file path MUST BE like this:
../file_storage/killbilly.sol
'''
def execute_audit(file_path):
    ## fileName string must include .sol extention
    file_path = "../file_storage/killbilly.sol"
    print(file_path)
    listOfvulnerabilities = []

    try:
        command = "cd ../slither\nslither " + file_path
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(command)
    except subprocess.CalledProcessError as e:
        #print("Command execution failed.")
        #print("Error message:", e.stderr)
        #print(type(e.stderr))
        output = e.stderr
        lines = output.split('\n')
        isRiskLine = False
        issueName = ""
        for line in lines:
            if line.startswith('INFO:Detectors:'):
                isRiskLine = True
                continue
            if line.startswith('Reference:'):
                Recommendation = find_solution(line[73:])
                
                Issue = {
                    "Issue": issueName,
                    "Suggestion": Recommendation
                }
                listOfvulnerabilities.append(Issue)
                issueName = ""
                isRiskLine = False
                
            if isRiskLine:
                issueName += line
                issueName += "\n"

    status = 'risky' if listOfvulnerabilities else 'safe'     
            
    return status, listOfvulnerabilities

def audit_smart_contract(db, file_name, file_content):
    date_time, file_path = store_file(file_name, file_content)

    #Audit logic goes here
    status, vulnerabilities = execute_audit(file_path)
    print(vulnerabilities)

    #Push audit result to db and store smart contract file
    audit_report = insert_audit_report(db, file_name, file_path, date_time, status, vulnerabilities)

    result = audit_report

    return response(201, "Success", result)

