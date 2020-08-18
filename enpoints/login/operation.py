from flask import jsonify

def check_name(name):
    if not name:
        return jsonify({})