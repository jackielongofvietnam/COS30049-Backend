from flask import session
import datetime

def store_smart_contract_file(file_name, file_content):
    user_id = session['user_id']
    timestamp = datetime.datetime.now().timestamp()
    dir = "file_storage"
    stored_file_name = f'{user_id}_{timestamp}_{file_name}'
    file_path = dir + '/' + stored_file_name

    try:  
        with open(file_path, 'w') as file:
            file.write(file_content)
        return True
    except:
        return False
