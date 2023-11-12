import os
import datetime
import pymongo

def insert_audit_report(db, user_id, file_name, file_path, date_time, status, vulnerabilities):
    # Insert audit report to db
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
    

def store_file(user_id, file_name, file_content):
    date_time = datetime.datetime.now()
    timestamp = date_time.timestamp()
    dir = "file_storage"

    # Combine user id and timestamp to file name to ensure its uniqueness
    stored_file_name = f'{user_id}_{timestamp}_{file_name}'
    file_path = dir + '/' + stored_file_name
    
    # Store smart contract file
    if not os.path.exists(dir):      
        os.makedirs(dir)
    try:  
        with open(file_path, 'w') as file:
            file.write(file_content)
    except:
        print('Failed to store smart contract!')

    return date_time, file_path


def get_audit_history_by_user_id(db, user_id, search):
    if search:
        result = db['Contracts'].find({"user_id": user_id, "file_name": {"$regex": search}}, {"_id": 0})
    else:
        result = db['Contracts'].find({"user_id": user_id}, {"_id": 0})
    
    # Create a audit history list from the query result
    audit_history = [doc for doc in result]

    return audit_history