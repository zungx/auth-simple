from flask import request, jsonify
from auth.auth_factory import AuthFactory
from auth.abstract_auth import AuthType


def request_access_token():
    rtk = request.json.get('refresh_token', 'None')
    auth = AuthFactory.get_auth(AuthType.WEB.value)
    result = auth.refresh(dict(refresh_token=rtk))

    if not result:
        return jsonify({
            'success': False,
            'message': 'Failed!'
        }), 400

    return jsonify({
        'success': True,
        'data': result
    }), 200
