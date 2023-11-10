from utilities.response import response
from data_access.contracts import insert_audit_report, store_file
import subprocess

def find_solution(sectionName):
    filePath = "slither/Detector-Documentation.md"
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
                          

def execute_audit(file_path):
    ## fileName string must include .sol extention
    listOfvulnerabilities = []

    try:
        command = "solc-select use 0.5.0\nslither " + file_path
        subprocess.run(command, shell=True, check=True, capture_output=True, text=True)   
    except subprocess.CalledProcessError as e:
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
                    "issue": issueName,
                    "suggestion": Recommendation
                }
                listOfvulnerabilities.append(Issue)
                issueName = ""
                isRiskLine = False
                
            if isRiskLine:
                issueName += line
                issueName += "\n"
    
    if listOfvulnerabilities:
        status = 'risky'
        for vulnerability in listOfvulnerabilities:
            vulnerability['issue'] = vulnerability['issue'].strip()
            vulnerability['suggestion'] = vulnerability['suggestion'].strip()
    else:
        status = 'safe'    
            
    return status, listOfvulnerabilities


def audit_smart_contract(db, user_id, file_name, file_content):
    date_time, file_path = store_file(user_id, file_name, file_content)

    #Audit logic goes here
    status, vulnerabilities = execute_audit(file_path)

    #Push audit result to db and store smart contract file
    insert_audit_report(db, user_id, file_name, file_path, date_time, status, vulnerabilities)
    audit_report = {
            "file_name": file_name,
            "date_uploaded": date_time,
            "status": status,
            "vulnerabilities": vulnerabilities
        }
    
    return response(201, "Success", audit_report)


