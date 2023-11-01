import subprocess

def findSolution(sectionName):
    filePath = "./slither/Detector-Documentation.md"
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
                
                
                
            

def Detect(fileName):
    ## fileName string must include .sol extention
    listOfvulnerabilities = []
    try:
        command = "cd slither\nslither " + fileName
         
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return listOfvulnerabilities
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
                Recommendation = findSolution(line[73:])
                
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
                
        return listOfvulnerabilities


# Example usage
FileName= input("Enter filename: ")
listOfvulnerabilities = Detect(FileName)

for risk in listOfvulnerabilities:
    print(risk)
    print()
    
