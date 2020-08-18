from flask import jsonify

def return_success_response(code=None,msg=None,data=None):
    res = {
        'code':code,
        'data':data,
        'msg':msg
    }
    return jsonify(res)


def return_error_response(code=None,msg=None,data=None):
    return jsonify({})

def return_xixi_response():
    return jsonify({'嘻嘻哈哈':'阿兜'})


def woshi():
    return jsonify({'我是':'大彪'})