from flask import jsonify
from exceptions.invalid_token import InvalidToken
from exceptions.token_expired import TokenExpired
from exceptions.token_revoked import TokenRevoked


def handle_exception(e):
    if isinstance(e, InvalidToken) or isinstance(e, TokenExpired) or isinstance(e, TokenRevoked):
        return jsonify(e.to_dict()), e.status_code

    # TODO: Handle other errors, HTTPException ( 405, 422,..)

    return jsonify({
        "message": "Internal server error",
        "status_code": e.status_code
    }), e.status_code
