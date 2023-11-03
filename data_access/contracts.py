import os
from flask import session
import datetime

import pymongo

def insert_audit_report(db, file_name, file_content, status, vulnerabilities):
    user_id = session['user_id']
    date_time = datetime.datetime.now()
    timestamp = date_time.timestamp()
    dir = "file_storage"
    stored_file_name = f'{user_id}_{timestamp}_{file_name}'
    file_path = dir + '/' + stored_file_name
    
    #Store smart contract file
    if not os.path.exists(dir):      
        os.makedirs(dir)
    try:  
        with open(file_path, 'w') as file:
            file.write(file_content)
    except:
        print('Failed to store smart contract!')
    
    #Insert audit report to db
    audit_report = {
        "user_id": user_id,
        "file_name": file_name,
        "file_path": file_path,
        "date_uploaded": date_time.strftime("%H:%M %d-%m-%Y"),
        "status": status,
        "vulnerabilities": vulnerabilities
    }
    try:
        db['Contracts'].insert_one(audit_report)
        insert_result = True
    except pymongo.errors.BulkWriteError as e:
        print(e)
        insert_result = False

    return insert_result
    

