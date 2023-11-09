from utilities.response import response
from data_access.contracts import get_audit_history_by_user_id

def search_audit_history(db, user_id, search):
    audit_history = get_audit_history_by_user_id(db, user_id, search)
    
    return response(200, "", audit_history)
