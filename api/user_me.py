from flask import request, jsonify
from api.middleware.user_auth import login_required


@login_required
def user_me():
    return jsonify({
        'success': True,
        'message': 'Ok',
        'data': {
            'user_id': int(request.user_auth['user_id'])
        }
    }), 200
