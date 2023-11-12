from utilities.response import response
from data_access.contracts import insert_audit_report, store_file
import subprocess

def find_solution(section_name):
    ## The function takes a string sectionName (error name)
    file_path = "slither/Detector-Documentation.md"
    '''Detector-Documentation.md is a markdown file with this structure:
# Public Detectors

List of public detectors

## Error1

### Description

### Exploit Scenario:

### Recommendation


## Error 2

### Description

### Exploit Scenario:

### Recommendation

    '''
    
    ## We need to find the line "## Error n" in the markdown file
    ## and find the subsection ### Recommendation
    ## Formating the name
    section_format = section_name.replace("-", " ")
    section_line_in_mark_down = "## " + section_format
    
    ## Open file "slither/Detector-Documentation.md"
    with open(file_path, 'r') as file:
        lines = file.readlines()
        found_out_section = False
        found_out_recommendation = False
        suggestions = ""
        
        ## Traversing every single line
        for line in lines:
            
            # if we found out the section
            if line.lower().startswith(section_line_in_mark_down):
                found_out_section = True
                continue
            
            if found_out_section and line.startswith("### Recommendation"):
                found_out_recommendation = True
                continue
            
            if found_out_recommendation and line.startswith("## "):
                return suggestions
            
            if found_out_recommendation:
                suggestions += line
                suggestions += "\n"
                  
    return "Currently can not find out the suggestions yet"
                          

def execute_audit(file_path):
    ## fileName string must include .sol extention
    list_of_vulnerabilities = []

    try:
        ## Run the command to select the solc version
        solc_select_command = "solc-select use 0.5.0"
        subprocess.run(solc_select_command, shell=True, check=True, capture_output=True, text=True)
        
        ## Using Slither commandline to audit the file
        audit_command = "slither " + file_path
        subprocess.run(audit_command, shell=True, check=True, capture_output=True, text=True)
        
        ## If the file is safe, then nothing happens
        ## but if there is an error, the terminal will raise the error   
        ## in almost cases, slither will raise an error in solidity file
    except subprocess.CalledProcessError as e:
        ## Get the error, as know as the output of slither
        output = e.stderr
        
        '''This is an example of output from Slither Library:
        INFO:Detectors:
        Example error 1
        Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#Recommendation-Example-error-1
        INFO:Detectors:
        Example error 2
        Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#Recommendation-Example-error-2
        '''
        
        ## Split the output into an array, each line will be an element
        lines = output.split('\n')
        
        ## Setting isRiskLine as False by default, 
        # a Risk Line always begins with 'INFO:Detectors:'
        is_risk_line = False
        issue_name = ""
        
        ## Traverse each line
        for line in lines:
            ## if the current line starts with 'INFO:Detectors:', 
            # setting isRiskLine to true, then check the next line
            if line.startswith('INFO:Detectors:'):
                is_risk_line = True
                continue
            
            ## if the current line starts with 'Reference'
            if line.startswith('Reference:'):
                ## find the section for the current issue
                # this reference line always begins with
                # Reference: https://github.com/crytic/slither/wiki/Detector-Documentation#
                # and is followed by the name of the error, all we need
                # to do is getting the name of current error 
                # and call function "find_solution()"
                recommendation = find_solution(line[73:])
                
                ## The function "find_solution" always returns a recommendation (string)
                # for the current error 
                
                ## Then, create an "Issue" object to store issue name and recommendation
                Issue = {
                    "issue": issue_name,
                    "suggestion": recommendation
                }
                
                ## appending the "Issue" object to the list of vulnerabilities
                list_of_vulnerabilities.append(Issue)
                
                ## Reset issueName and isRiskLine
                issue_name = ""
                is_risk_line = False
            
            ## If the current line is riskline, 
            # then append it to the issueName string 
            if is_risk_line:
                issue_name += line
                issue_name += "\n"
    
    # Determine whether the smart contract is safe or risky
    if list_of_vulnerabilities:
        status = 'risky'
        for vulnerability in list_of_vulnerabilities:
            # Remove break line in the 2 ends of the string
            vulnerability['issue'] = vulnerability['issue'].strip()
            vulnerability['suggestion'] = vulnerability['suggestion'].strip()
    else:
        status = 'safe'    
            
    return status, list_of_vulnerabilities


def audit_smart_contract(db, user_id, file_name, file_content):
    # Store smart contract file
    date_time, file_path = store_file(user_id, file_name, file_content)

    # Audit logic goes here
    status, vulnerabilities = execute_audit(file_path)

    # Push audit result to db
    insert_audit_report(db, user_id, file_name, file_path, date_time, status, vulnerabilities)
    audit_report = {
            "file_name": file_name,
            "date_uploaded": date_time,
            "status": status,
            "vulnerabilities": vulnerabilities
        }
    
    return response(201, "Success", audit_report)