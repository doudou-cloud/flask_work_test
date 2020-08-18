from flask import jsonify

def return_success_response(code=None,msg=None,data=None):
    res = {
        'code':code,
        'data':data,
        'msg':msg
    }
    return jsonify(res)

