from flask import jsonify


def health():
    return jsonify({
        "success": True,
        'message': "OK"
    }), 200
