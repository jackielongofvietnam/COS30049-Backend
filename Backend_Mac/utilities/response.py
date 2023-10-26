from flask import jsonify

def response(statusCode, message="", data=None):
    return jsonify({
        'status': statusCode,
        'message': message,
        'data': data
    })