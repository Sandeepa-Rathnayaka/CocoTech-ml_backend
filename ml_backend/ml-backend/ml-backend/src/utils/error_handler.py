from flask import jsonify

class APIError(Exception):
    def __init__(self, message, status_code=400):
        super().__init__()
        self.message = message
        self.status_code = status_code

def handle_error(error):
    if isinstance(error, APIError):
        response = jsonify({
            'error': error.message,
            'status_code': error.status_code
        })
        response.status_code = error.status_code
        return response
    
    # Handle unexpected errors
    response = jsonify({
        'error': 'Internal Server Error',
        'status_code': 500
    })
    response.status_code = 500
    return response