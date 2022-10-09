from flask import request, jsonify
from auth.auth_factory import AuthFactory
from auth.abstract_auth import AuthType


def do_login():
    username = request.json.get('username', '')
    password = request.json.get('password', '')
    auth = AuthFactory.get_auth(AuthType.WEB.value)
    result = auth.login(dict(username=username, password=password))

    if not result:
        return jsonify({
            'success': False,
            'message': 'Failed!'
        }), 400

    return jsonify({
        "success": True,
        "data": result
    }), 200
